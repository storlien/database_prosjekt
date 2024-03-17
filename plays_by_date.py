import sqlite3
    
def find_plays(date):
    con = sqlite3.connect("teater.db")
    cur = con.cursor()
    cur.execute(f"SELECT Teaterstykke.Tittel, Forestilling.Tid, COUNT(Billett.BillettID) FROM Forestilling LEFT JOIN Billett ON Forestilling.ForestillingNr = Billett.ForestillingNr INNER JOIN Teaterstykke ON Teaterstykke.StykkeID = Forestilling.StykkeID WHERE Forestilling.Dato = '{date}' GROUP BY Forestilling.ForestillingNr")
    for row in cur.fetchall():
        print(f"Forestilling: {row[0]}, {row[1]}. Antall billetter solgt: {row[2]}")

