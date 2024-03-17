import sqlite3

section_id = {
        "Parkett": 3,
        "Balkong": 4,
        "Galleri": 5
    }

def reserve_seats(db, section, bought_seats):

    con = sqlite3.connect(db)
    cur = con.cursor()

    id = section_id[section]

    for seat_tuple in bought_seats:
        cur.execute("INSERT INTO Billett (StykkeID, ForestillingNr, OmraadeID, SeteNr, RadNr) VALUES (2, 1, :section, :seat_number, :row_number)", {"section": id, "seat_number": seat_tuple[1], "row_number": seat_tuple[0]})
    
    con.commit()
    con.close()

    print("Seats reserved in section", section)