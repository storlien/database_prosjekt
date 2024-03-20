import sys, config
import sqlite3

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
    print("Parkett section ID:", config.GAMLE_SCENE_PARKETT_SECTION_ID)
    print("Balkong section ID:", config.GAMLE_SCENE_BALKONG_SECTION_ID)
    print("Galleri section ID:", config.GAMLE_SCENE_GALLERI_SECTION_ID)

    con = sqlite3.connect(db)
    cur = con.cursor()

    # Parkett
    for rowNo in range(1, 11):
        
        for seatNo in range(1, config.NO_SEATS_GAMLE_SCENE_PARKETT.get(rowNo) + 1):
            con.execute(f"INSERT INTO Sete (SeteNr, RadNr, OmraadeID) VALUES ({seatNo}, {rowNo}, {config.GAMLE_SCENE_PARKETT_SECTION_ID})")

    # Balkong
    for rowNo in range(1, 5):
        
        for seatNo in range(1, config.NO_SEATS_GAMLE_SCENE_BALKONG.get(rowNo) + 1):
            con.execute(f"INSERT INTO Sete (SeteNr, RadNr, OmraadeID) VALUES ({seatNo}, {rowNo}, {config.GAMLE_SCENE_BALKONG_SECTION_ID})")
  
    # Galleri
    for rowNo in range(1, 4):
        
        for seatNo in range(1, config.NO_SEATS_GAMLE_SCENE_GALLERI.get(rowNo) + 1):
            con.execute(f"INSERT INTO Sete (SeteNr, RadNr, OmraadeID) VALUES ({seatNo}, {rowNo}, {config.GAMLE_SCENE_GALLERI_SECTION_ID})")
    
    con.commit()
    con.close()

    print("Seats successfully inserted into the database!")
    print()

if __name__ == "__main__":
    main()