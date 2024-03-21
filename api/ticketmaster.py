import sqlite3, config
from datetime import datetime

from api.validator import Validator


class TicketMaster:

    def __init__(self, db_path=config.DEFAULT_DB):
        self.db_path = db_path
        self.validator = Validator(db_path)

    def get_play_id(self, play_name, season_id):
        with sqlite3.connect(self.db_path) as con:
            cur = con.cursor()
            cur.execute(
                """
                SELECT StykkeID
                FROM Teaterstykke
                WHERE Tittel = ? AND SesongID = ?
                """,
                (play_name, season_id),
            )
            return cur.fetchone()

    def get_section_ids(self, play_id):
        with sqlite3.connect(self.db_path) as con:
            cur = con.cursor()
            cur.execute(
                """
                SELECT Omraade.Navn, Omraade.OmraadeID
                FROM Omraade
                INNER JOIN Teatersal ON Omraade.SalNr = Teatersal.SalNr
                INNER JOIN Teaterstykke ON Teatersal.SalNr = Teaterstykke.SalNr
                WHERE Teaterstykke.StykkeID = ?
                """,
                (play_id,),
            )
            return dict(cur.fetchall())

    def get_play_id_and_act_no(self, play_name, date):
        with sqlite3.connect(self.db_path) as con:
            cur = con.cursor()
            cur.execute(
                """
                SELECT Teaterstykke.StykkeID, Forestilling.ForestillingNr
                FROM Teaterstykke
                INNER JOIN Forestilling ON Teaterstykke.StykkeID = Forestilling.StykkeID
                WHERE Tittel = ? AND Dato = ?
                """,
                (play_name, date),
            )
            return cur.fetchone()

    def find_available_seats_for_play(self, section_id, n_seats_requested, play_id, act_no):
        with sqlite3.connect(self.db_path) as con:
            cur = con.cursor()
            cur.execute(
                """
                SELECT RadNr, COUNT(*) as AvailableSeats
                FROM Sete
                WHERE OmraadeID = ?
                AND (SeteNr, RadNr, OmraadeID) NOT IN (
                    SELECT SeteNr, RadNr, OmraadeID
                    FROM Billett
                    WHERE StykkeID = ? AND ForestillingNr = ?
                )
                GROUP BY RadNr
                HAVING COUNT(*) >= ?
                """,
                (section_id, play_id, act_no, n_seats_requested),
            )
            rows = cur.fetchall()

        return rows[0][0] if rows else None

    def check_customer_exists(self, phone_number):
        with sqlite3.connect(self.db_path) as con:
            cur = con.cursor()
            cur.execute("SELECT Navn, Adresse FROM KundeProfil WHERE Mobilnummer = ?", (phone_number,))
            result = cur.fetchone()
            if result:
                navn, adresse = result
                return navn, adresse
            else:
                return None, None

    def check_and_add_customer(self, phone_number, name, address):
        with sqlite3.connect(self.db_path) as con:
            cur = con.cursor()
            cur.execute("SELECT * FROM KundeProfil WHERE Mobilnummer = ?", (phone_number,))
            if cur.fetchone() is None:
                cur.execute(
                    "INSERT INTO KundeProfil (Mobilnummer, Navn, Adresse) VALUES (?, ?, ?)",
                    (phone_number, name, address),
                )
                con.commit()
            return cur.fetchone() is None

    def create_billett_kjop(self, phone_number):
        with sqlite3.connect(self.db_path) as con:
            cur = con.cursor()
            cur.execute(
                "INSERT INTO BillettKjop (Tid, Dato, Mobilnummer) VALUES (time('now'), date('now'), ?)", (phone_number,)
            )
            return cur.lastrowid

    def reserve_seats(
        self,
        kjop_id: int,
        section_id: int,
        row_number: int,
        n: int,
        play_id: int,
        act_no: int,
        customer_groups: list[str],
    ):
        with sqlite3.connect(self.db_path) as con:
            cur = con.cursor()
            for group in customer_groups:
                cur.execute(
                    """
                    INSERT INTO Billett (KjopID, StykkeID, ForestillingNr, OmraadeID, SeteNr, RadNr, KundeGruppe)
                    SELECT ?, ?, ?, ?, SeteNr, ?, ?
                    FROM Sete
                    WHERE OmraadeID = ? AND RadNr = ? AND SeteNr NOT IN (
                        SELECT SeteNr
                        FROM Billett
                        WHERE StykkeID = ? AND ForestillingNr = ? AND OmraadeID = ? AND RadNr = ?
                    )
                    LIMIT 1
                    """,
                    (
                        kjop_id,
                        play_id,
                        act_no,
                        section_id,
                        row_number,
                        group,
                        section_id,
                        row_number,
                        play_id,
                        act_no,
                        section_id,
                        row_number,
                    ),
                )
            con.commit()

    def purchase_tickets(
        self, play_name, date_str, section, n, phone_number, customer_name, customer_address, customer_groups
    ):
        try:
            date = datetime.strptime(date_str, "%Y-%m-%d").strftime("%Y-%m-%d")
        except ValueError:
            return "Ugyldig datoformat. Vennligst bruk ÅÅÅÅ-MM-DD."

        play_id, act_no = self.get_play_id_and_act_no(play_name, date)
        if play_id is None or act_no is None:
            return "Forestillingen eller fremføringen ble ikke funnet."

        section_ids = self.get_section_ids(play_id)
        section_id = section_ids.get(section)

        if section_id is None:
            available_sections = ", ".join(section_ids.keys())
            return f"Seksjonen '{section}' eksisterer ikke for dette stykket. Tilgjengelige seksjoner: {available_sections}"

        row_number = self.find_available_seats_for_play(section_id, n, play_id, act_no)
        if row_number is not None:
            self.check_and_add_customer(phone_number, customer_name, customer_address)
            kjop_id = self.create_billett_kjop(phone_number)
            self.reserve_seats(kjop_id, section_id, row_number, n, play_id, act_no, customer_groups)
            return (
                f"{n} billetter reservert i seksjon {section} på rad {row_number} for '{play_name}' den {date}.",
                kjop_id,
            )
        else:
            return "Ingen tilgjengelige seter funnet.", None

    def admin_create_billett_kjop(self):
        return self.create_billett_kjop(config.ADMIN_PHONE_NUMBER)

    def admin_reserve_tickets(
        self, play_name: str, date: str, section: str, bought_seats: list, kjop_id: int = None, season_id: int = 1
    ):
        if kjop_id is None:
            kjop_id = self.create_billett_kjop(config.ADMIN_PHONE_NUMBER)

        play_id, act_no = self.get_play_id_and_act_no(play_name, date)

        for row_number, seat_number in bought_seats:
            self.reserve_single_seat(kjop_id, play_id, act_no, section, seat_number, row_number, "Admin")

    def reserve_single_seat(
        self, kjop_id: int, play_id: int, act_id: int, section_id: int, seat_no: int, row_no: int, customer_group: str
    ):
        with sqlite3.connect(self.db_path) as con:
            cur = con.cursor()
            cur.execute(
                """
                INSERT INTO Billett (KjopID, StykkeID, ForestillingNr, KundeGruppe, OmraadeID, SeteNr, RadNr)
                VALUES (?, ?, ?, ?, ?, ?, ?)
                """,
                (kjop_id, play_id, act_id, customer_group, section_id, seat_no, row_no),
            )
            con.commit()

    # seats_to_reserve is a tuple with play_id, act_no, customer_group, section_id, row_no, seat_no to be reserved
    def reserve_seat_list(self, kjop_id: int, seats_to_reserve: list):
        with sqlite3.connect(self.db_path) as con:
            cur = con.cursor()
            for seat in seats_to_reserve:
                cur.execute(
                    """
                    INSERT INTO Billett (KjopID, StykkeID, ForestillingNr, KundeGruppe, OmraadeID, SeteNr, RadNr)
                    VALUES (?, ?, ?, ?, ?, ?, ?)
                    """,
                    (
                        kjop_id,
                        *seat,
                    ),
                )
            con.commit()

    def which_play(self, hall, date, season_id):
        with sqlite3.connect(self.db_path) as con:
            cur = con.cursor()
            cur.execute(
                """
                SELECT Tittel
                FROM Teaterstykke
                WHERE SalNr = (SELECT SalNr FROM Teatersal WHERE SalNavn = ?)
                AND StykkeID IN (
                    SELECT StykkeID
                    FROM Forestilling
                    WHERE Dato = ?
                ) AND SesongID = ?
                """,
                (hall, date, season_id),
            )
            return cur.fetchone()
