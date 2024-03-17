import sqlite3

'''
Finds the actors that play in the same act as input actor and prints the title of the play and the actors.
'''
def actors_same_act(actor) -> None:
    con = sqlite3.connect("teater.db")
    cur = con.cursor()
    cur.execute(f'''SELECT DISTINCT Akt.StykkeID, Akt.AktNr
                FROM Akt JOIN PaaAkt ON Akt.StykkeID = PaaAkt.StykkeID AND Akt.AktNr = PaaAkt.AktNr
                JOIN SpillerRolle ON PaaAkt.RolleID = SpillerRolle.RolleID
                JOIN Ansatt ON SpillerRolle.AnsattID = Ansatt.AnsattID
                WHERE Ansatt.Navn = '{actor}'
                ''')
    actor_acts = cur.fetchall()

    for act in actor_acts:
        cur.execute(f'''SELECT DISTINCT Teaterstykke.Tittel, Akt.Navn, Ansatt.Navn
                FROM Akt JOIN PaaAkt ON Akt.StykkeID = PaaAkt.StykkeID AND Akt.AktNr = PaaAkt.AktNr
                JOIN SpillerRolle ON PaaAkt.RolleID = SpillerRolle.RolleID
                JOIN Ansatt ON SpillerRolle.AnsattID = Ansatt.AnsattID
                JOIN Teaterstykke ON Akt.StykkeID = Teaterstykke.StykkeID
                WHERE Akt.StykkeID = {act[0]} AND Akt.AktNr = {act[1]} AND Ansatt.Navn != '{actor}'
                ''')
        for row in cur.fetchall():
            print(f"Stykke: {row[0]} i akt {row[1]} med {row[2]}:")
            
actors_same_act("Synnøve Fossum Eriksen")