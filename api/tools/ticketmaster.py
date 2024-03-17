import sqlite3
from datetime import datetime


class TicketMaster:
    def __init__(self, db_path="theatre.sqlite"):
        self.db_path = db_path

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

    def create_billett_kjop(self, phone_number):
        with sqlite3.connect(self.db_path) as con:
            cur = con.cursor()
            cur.execute(
                "INSERT INTO BillettKjop (Tid, Dato, Mobilnummer) VALUES (time('now'), date('now'), ?)", (phone_number,)
            )
            return cur.lastrowid

    def reserve_seats(self, kjop_id, section_id, row_number, n, play_id, act_no, customer_group):
        with sqlite3.connect(self.db_path) as con:
            cur = con.cursor()
            for _ in range(n):
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
                        customer_group,
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
        self, play_name, date_str, section, n, phone_number, customer_name, customer_address, customer_group
    ):
        try:
            date = datetime.strptime(date_str, "%Y-%m-%d").strftime("%Y-%m-%d")
        except ValueError:
            return "Invalid date format. Please use YYYY-MM-DD."

        play_id, act_no = self.get_play_id_and_act_no(play_name, date)
        if play_id is None or act_no is None:
            return "Play or performance not found."

        section_ids = self.get_section_ids(play_id)
        section_id = section_ids.get(section)

        if section_id is None:
            available_sections = ", ".join(section_ids.keys())
            return f"Section '{section}' does not exist for this play. Available sections: {available_sections}"

        row_number = self.find_available_seats_for_play(section_id, n, play_id, act_no)
        if row_number is not None:
            self.check_and_add_customer(phone_number, customer_name, customer_address)
            kjop_id = self.create_billett_kjop(phone_number)
            self.reserve_seats(kjop_id, section_id, row_number, n, play_id, act_no, customer_group)
            return f"{n} tickets reserved in section {section} on row {row_number} for '{play_name}' on {date}."
        else:
            return "No available seats found."


# Example usage:
# ticket_master = TicketMaster('database.db')
# print(ticket_master.purchase_tickets('STØRST AV ALT ER KJÆRLIGHETEN', '2024-02-03',
