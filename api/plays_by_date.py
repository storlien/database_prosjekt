import sqlite3
    
'''
Finds all plays on a given date and prints the title of the play, the time of the play and the number of tickets sold for the play.
Template: find_plays("2024-02-03")
'''
def find_plays(date):
    con = sqlite3.connect("teater.db")
    cur = con.cursor()
    cur.execute(f'''SELECT Teaterstykke.Tittel, Forestilling.Tid, COUNT(Billett.BillettID) 
                FROM Forestilling LEFT OUTER JOIN Billett ON Forestilling.ForestillingNr = Billett.ForestillingNr 
                INNER JOIN Teaterstykke ON Teaterstykke.StykkeID = Forestilling.StykkeID 
                WHERE Forestilling.Dato = '{date}' 
                GROUP BY Forestilling.ForestillingNr''')
    print(f"{'-' * 10} Forestillinger {date} {'-' * 10}")
    for row in cur.fetchall():
        print(f"{row[0]}, {row[1]} | Billetter solgt: {row[2]}")
    
    con.close()

find_plays("2024-02-03")