import sys
import sqlite3

PARKETT_SECTION_ID = 3
BALKONG_SECTION_ID = 4
GALLERI_SECTION_ID = 5

NO_SEATS_PARKETT = {
    1: 18,
    2: 16,
    3: 17,
    4: 18,
    5: 18,
    6: 17,
    7: 18,
    8: 17,
    9: 17,
    10: 14
}

NO_SEATS_BALKONG = {
    1: 28,
    2: 27,
    3: 22,
    4: 17
}

NO_SEATS_GALLERI = {
    1: 33,
    2: 18,
    3: 17
}

def main():
    arguments = sys.argv[1:]

    if len(arguments) == 0:
        print("Missing argument")
        print("Usage: python3 insert_seats_gamle_scene.py <database.db>")
        return
    
    elif len(arguments) > 1:
        print("Too many arguments")
        print("Usage: python3 insert_seats_gamle_scene.py <database.db>")
        return
    
    db = arguments[0].strip()

    insert_seats(db)

def insert_seats(db):

    print("Inserting seats into the database...")
    print("Database file:", db)
    print("Parkett section ID:", PARKETT_SECTION_ID)
    print("Balkong section ID:", BALKONG_SECTION_ID)
    print("Galleri section ID:", GALLERI_SECTION_ID)

    con = sqlite3.connect(db)
    cur = con.cursor()

    # Parkett
    for rowNo in range(1, 11):
        
        for seatNo in range(1, NO_SEATS_PARKETT.get(rowNo) + 1):
            con.execute(f"INSERT INTO Sete (SeteNr, RadNr, OmraadeID) VALUES ({seatNo}, {rowNo}, {PARKETT_SECTION_ID})")

    # Balkong
    for rowNo in range(1, 5):
        
        for seatNo in range(1, NO_SEATS_BALKONG.get(rowNo) + 1):
            con.execute(f"INSERT INTO Sete (SeteNr, RadNr, OmraadeID) VALUES ({seatNo}, {rowNo}, {BALKONG_SECTION_ID})")
  
    # Galleri
    for rowNo in range(1, 4):
        
        for seatNo in range(1, NO_SEATS_GALLERI.get(rowNo) + 1):
            con.execute(f"INSERT INTO Sete (SeteNr, RadNr, OmraadeID) VALUES ({seatNo}, {rowNo}, {GALLERI_SECTION_ID})")
    
    con.commit()
    con.close()

    print("Seats successfully inserted into the database!")
    print()

if __name__ == "__main__":
    main()