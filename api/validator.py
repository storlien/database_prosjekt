import sqlite3, config

class Validator:
    def __init__(self, db_path=config.DEFAULT_DB):
        self.db_path = db_path
    
    def validate_play_name(self, play_name: str):
        with sqlite3.connect(self.db_path) as con:
            cur = con.cursor()
            cur.execute("SELECT * FROM Teaterstykke WHERE Tittel = ?", (play_name,))
            return cur.fetchone() is not None

    def validate_hall(self, hall: str):
        with sqlite3.connect(self.db_path) as con:
            cur = con.cursor()
            cur.execute("SELECT * FROM Teatersal WHERE SalNavn = ?", (hall,))
            return cur.fetchone() is not None
    
    def validate_section(self, hall, section: str):
        with sqlite3.connect(self.db_path) as con:
            cur = con.cursor()
            cur.execute("SELECT * FROM Teatersal WHERE SalNavn = ?", (hall,))
            hall_id = cur.fetchone()[0]
            cur.execute("SELECT * FROM Omraade WHERE Navn = ? AND SalNr = ?", (section,hall_id))
            return cur.fetchone() is not None