import sqlite3

'''
Finds all plays and the number of tickets sold for the play and prints the title of the play and the number of tickets sold.
Sorted on number of tickets sold in ascending order.
'''
def tickets_sold(db: str = "teater.db"):
    con = sqlite3.connect(db)
    cur = con.cursor()
    cur.execute('''SELECT Teaterstykke.Tittel, Forestilling.Dato, COUNT(Billett.BillettID) 
                FROM Forestilling LEFT OUTER JOIN Billett ON Forestilling.StykkeID = Billett.StykkeID AND Forestilling.ForestillingNr = Billett.ForestillingNr
                INNER JOIN Teaterstykke ON Teaterstykke.StykkeID = Forestilling.StykkeID
                GROUP BY Forestilling.ForestillingNr 
                ORDER BY COUNT(Billett.BillettID)''')
    
    print(f"{'-' * 10} Forestillinger og antall billetter solgt {'-' * 10}")
    for row in cur.fetchall():
        print(f" {row[0]}, {row[1]} | Billetter solgt: {row[2]}")
        
    con.close()
    
tickets_sold()