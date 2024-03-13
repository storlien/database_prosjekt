import sqlite3

DB = "tester_gamle_scene.db"

con = sqlite3.connect(DB)
cur = con.cursor()

def reserve_seats(section, bought_seats):
    print(section, bought_seats)