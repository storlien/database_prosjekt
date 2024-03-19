import sqlite3


class PriceCalculator:
    def __init__(self, db_path="teater.sqlite"):
        self.db_path = db_path

    def get_purchase_id(self, phone_number, play_name, date):
        with sqlite3.connect(self.db_path) as con:
            cur = con.cursor()
            cur.execute(
                """
                SELECT BillettKjop.KjopID
                FROM BillettKjop
                INNER JOIN Billett ON BillettKjop.KjopID = Billett.KjopID
                INNER JOIN Forestilling ON Billett.StykkeID = Forestilling.StykkeID
                INNER JOIN Teaterstykke ON Forestilling.StykkeID = Teaterstykke.StykkeID
                WHERE BillettKjop.Mobilnummer = ? AND Teaterstykke.Tittel = ? AND Forestilling.Dato = ?
                """,
                (phone_number, play_name, date),
            )
            result = cur.fetchone()
            return result[0] if result else None

    def calculate_total_price(self, kjop_id):
        total_price = 0
        with sqlite3.connect(self.db_path) as con:
            cur = con.cursor()
            cur.execute(
                """
                SELECT KundeGruppe, StykkeID, COUNT(*) as TicketCount
                FROM Billett
                WHERE KjopID = ?
                GROUP BY KundeGruppe, StykkeID
                """,
                (kjop_id,),
            )
            for row in cur.fetchall():
                kunde_gruppe, stykke_id, count = row
                cur.execute(
                    """
                    SELECT Pris
                    FROM BillettPriser
                    WHERE GruppeNavn = ? AND StykkeID = ?
                    """,
                    (kunde_gruppe, stykke_id),
                )
                price_result = cur.fetchone()
                if price_result:
                    total_price += price_result[0] * count
        return total_price

    def get_purchase_price(self, phone_number, play_name, date):
        kjop_id = self.get_purchase_id(phone_number, play_name, date)
        if kjop_id is None:
            return "No purchase found."
        total_price = self.calculate_total_price(kjop_id)
        return f"Total price for the purchase: {total_price}"
