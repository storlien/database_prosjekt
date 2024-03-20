import sqlite3


## Alle brukerhistoriene er implementert i funksjoner under.

'''
Finds all actors and the roles they play in the plays and prints the title of the play, the role and the actor.
''' 
def find_actors(db: str = "teater.db"):
    con = sqlite3.connect(db)
    cur = con.cursor()
    cur.execute('''SELECT DISTINCT Teaterstykke.Tittel, Ansatt.Navn, Rolle.Navn 
                FROM Teaterstykke JOIN PaaAkt ON Teaterstykke.StykkeID = PaaAkt.StykkeID 
                JOIN Rolle ON PaaAkt.RolleID = Rolle.RolleID 
                JOIN SpillerRolle ON PaaAkt.RolleID = SpillerRolle.RolleID 
                JOIN Ansatt ON SpillerRolle.AnsattID = Ansatt.AnsattID''')
    
    print(f"{'-' * 10} Skuespillere og roller {'-' * 10}")
    for row in cur.fetchall():
        print(f"Stykke: {row[0]} \nRolle: {row[2]} \nSkuespiller: {row[1]}")
        print("-")
        
    con.close()
    
# find_actors()


'''
Finds the actors that play in the same act as input actor and prints the title of the play and the actors.
'''
def actors_same_act(actor, db: str = "teater.db") -> None:
    con = sqlite3.connect(db)
    cur = con.cursor()
    cur.execute(f'''SELECT DISTINCT Akt.StykkeID, Akt.AktNr
                FROM Akt JOIN PaaAkt ON Akt.StykkeID = PaaAkt.StykkeID AND Akt.AktNr = PaaAkt.AktNr
                JOIN SpillerRolle ON PaaAkt.RolleID = SpillerRolle.RolleID
                JOIN Ansatt ON SpillerRolle.AnsattID = Ansatt.AnsattID
                WHERE Ansatt.Navn = '{actor}'
                ''')
    actor_acts = cur.fetchall()

    print(f"{'-' * 5} Skuespillere som spiller i samme akt som {actor} {'-' * 5}")
    
    for act in actor_acts:
        cur.execute(f'''SELECT DISTINCT Teaterstykke.Tittel, Akt.Navn, Ansatt.Navn
                FROM Akt JOIN PaaAkt ON Akt.StykkeID = PaaAkt.StykkeID AND Akt.AktNr = PaaAkt.AktNr
                JOIN SpillerRolle ON PaaAkt.RolleID = SpillerRolle.RolleID
                JOIN Ansatt ON SpillerRolle.AnsattID = Ansatt.AnsattID
                JOIN Teaterstykke ON Akt.StykkeID = Teaterstykke.StykkeID
                WHERE Akt.StykkeID = {act[0]} AND Akt.AktNr = {act[1]} AND Ansatt.Navn != '{actor}'
                ''')
        for row in cur.fetchall():
            print(f"Stykke: {row[0]} \nakt: {row[1]} \nSkuespiller: {row[2]}")
            print("-")
                        
    con.close()
    
# actors_same_act("Synnøve Fossum Eriksen")

def actors_same_act2(actor, db: str = "teater.db") -> None:
    con = sqlite3.connect(db)
    cur = con.cursor()
    query = f"""
        SELECT DISTINCT Teaterstykke.Tittel, Akt.AktNr, Ansatt.Navn
        FROM Ansatt
        JOIN SpillerRolle ON Ansatt.AnsattID = SpillerRolle.AnsattID
        JOIN PaaAkt ON SpillerRolle.RolleID = PaaAkt.RolleID
        JOIN Akt ON PaaAkt.StykkeID = Akt.StykkeID AND PaaAkt.AktNr = Akt.AktNr
        JOIN Teaterstykke ON Akt.StykkeID = Teaterstykke.StykkeID
        WHERE Akt.StykkeID IN (
            SELECT Akt.StykkeID
            FROM Ansatt
            JOIN SpillerRolle ON Ansatt.AnsattID = SpillerRolle.AnsattID
            JOIN PaaAkt ON SpillerRolle.RolleID = PaaAkt.RolleID
            JOIN Akt ON PaaAkt.StykkeID = Akt.StykkeID AND PaaAkt.AktNr = Akt.AktNr
            WHERE Ansatt.Navn = '{actor}'
        ) AND Akt.AktNr IN (
            SELECT Akt.AktNr
            FROM Ansatt
            JOIN SpillerRolle ON Ansatt.AnsattID = SpillerRolle.AnsattID
            JOIN PaaAkt ON SpillerRolle.RolleID = PaaAkt.RolleID
            JOIN Akt ON PaaAkt.StykkeID = Akt.StykkeID AND PaaAkt.AktNr = Akt.AktNr
            WHERE Ansatt.Navn = '{actor}'
        ) AND Ansatt.Navn != '{actor}'
        ORDER BY Teaterstykke.Tittel, Akt.AktNr, Ansatt.Navn
    """
    cur.execute(query)
    results = cur.fetchall()

    print(f"{'-' * 5} Skuespillere som spiller i samme akt som {actor} {'-' * 5}")
    
    for row in results:
        print(f"Stykke: {row[0]} \nAkt: {row[1]} \nSkuespiller: {row[2]}")
        print("-")
                        
    con.close()

'''
Finds all plays on a given date and prints the title of the play, the time of the play and the number of tickets sold for the play.
Template: find_plays("2024-02-03")
'''
def find_plays(date, db: str = "teater.db"):
    con = sqlite3.connect(db)
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

# find_plays("2024-02-03")

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