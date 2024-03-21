import sqlite3
import sys
import os


sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import config

"""

Brukstilfelle 4

Finds all plays on a given date and prints the title of the play, the time of the play and the number of tickets sold for the play.
Template: find_plays("2024-02-03")

"""


def find_plays(date, db: str = config.DEFAULT_DB):
    con = sqlite3.connect(db)
    cur = con.cursor()
    cur.execute(
        f"""SELECT Teaterstykke.Tittel, Forestilling.Tid, COUNT(Billett.BillettID) 
                FROM Forestilling LEFT OUTER JOIN Billett ON Forestilling.ForestillingNr = Billett.ForestillingNr 
                INNER JOIN Teaterstykke ON Teaterstykke.StykkeID = Forestilling.StykkeID 
                WHERE Forestilling.Dato = '{date}' 
                GROUP BY Forestilling.ForestillingNr"""
    )
    print(f"{'-' * 10} Forestillinger {date} {'-' * 10}")
    for row in cur.fetchall():
        print(f"{row[0]}, {row[1]} | Billetter solgt: {row[2]}")

    con.close()


input = input("Hvilken dato vil du finne forestillinger for? (YYYY-MM-DD), default er 2024-02-03:")

if input.strip() == "":
    input = "2024-02-03"
    print("Default brukt: 2024-02-03\n")

find_plays(input)
