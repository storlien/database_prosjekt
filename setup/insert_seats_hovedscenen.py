import sys
import sqlite3

PARKETT_SECTION_ID = 1
GALLERI_SECTION_ID = 2

unavailable_seats = [467,468,469,470,495,496,497,498]

def main():
    arguments = sys.argv[1:]

    if len(arguments) == 0:
        print("Missing argument")
        print("Usage: python3 insert_seats_hovedscenen.py <database.db>")
        return
    
    elif len(arguments) > 1:
        print("Too many arguments")
        print("Usage: python3 insert_seats_hovedscenen.py <database.db>")
        return
    
    db = arguments[0].strip()

    insert_seats(db)

def insert_seats(db):

    print("Inserting seats into the database...")
    print("Database file:", db)
    print("Hovedscenen section ID:", PARKETT_SECTION_ID)
    print("Galleri section ID:", GALLERI_SECTION_ID)

    con = sqlite3.connect(db)
    cur = con.cursor()

    # Parkett
    for seatNo in range(1, 505):
        rowNo = (seatNo-1)//28 + 1

        if seatNo in unavailable_seats:
            continue

        con.execute(f"INSERT INTO Sete (SeteNr, RadNr, OmraadeID) VALUES ({seatNo}, {rowNo}, {PARKETT_SECTION_ID})")

    # Galleri
    for seatNo in range(505,525):
        rowNo = (seatNo-505)//5 + 1
        con.execute(f"INSERT INTO Sete (SeteNr, RadNr, OmraadeID) VALUES ({seatNo}, {rowNo}, {GALLERI_SECTION_ID})")
  
    con.commit()
    con.close()

    print("Seats successfully inserted into the database!")
    print()

if __name__ == "__main__":
    main()