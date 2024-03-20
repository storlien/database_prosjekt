import sqlite3, config

'''

Brukstilfelle 6

Finds all plays and the number of tickets sold for the play and prints the title of the play and the number of tickets sold.
Sorted on number of tickets sold in descending order.

'''
def tickets_sold(db: str = config.DEFAULT_DB):
    con = sqlite3.connect(db)
    cur = con.cursor()
    cur.execute('''SELECT Teaterstykke.Tittel, Forestilling.Dato, Forestilling.Tid, COUNT(Billett.BillettID) 
                FROM Forestilling LEFT OUTER JOIN Billett ON Forestilling.StykkeID = Billett.StykkeID AND Forestilling.ForestillingNr = Billett.ForestillingNr
                INNER JOIN Teaterstykke ON Teaterstykke.StykkeID = Forestilling.StykkeID
                GROUP BY Teaterstykke.Tittel, Forestilling.ForestillingNr 
                ORDER BY COUNT(Billett.BillettID) DESC''')
    
    print(f"{'-' * 10} Forestillinger og antall billetter solgt. Sortert synkende. {'-' * 10}")
    for row in cur.fetchall():
        print(f" {row[0]} | {row[1]} | {row[2]} | Billetter solgt: {row[3]} ")
        
    con.close()

tickets_sold()