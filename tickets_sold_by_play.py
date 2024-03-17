import sqlite3

'''
Finds all plays and the number of tickets sold for the play and prints the title of the play and the number of tickets sold.
Sorted on number of tickets sold in ascending order.
'''
def tickets_sold():
    con = sqlite3.connect("teater.db")
    cur = con.cursor()
    cur.execute('''SELECT Teaterstykke.Tittel, Forestilling.Dato, COUNT(Billett.BillettID) 
                FROM Forestilling LEFT OUTER JOIN Billett ON Forestilling.StykkeID = Billett.StykkeID AND Forestilling.ForestillingNr = Billett.ForestillingNr
                INNER JOIN Teaterstykke ON Teaterstykke.StykkeID = Forestilling.StykkeID
                GROUP BY Forestilling.ForestillingNr 
                ORDER BY COUNT(Billett.BillettID)''')
    for row in cur.fetchall():
        print(f"Forestilling: {row[0]}, Dato: {row[1]} Antall billetter solgt: {row[2]}")
        
tickets_sold()