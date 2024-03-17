import sqlite3

'''
Finds all actors and the roles they play in the plays and prints the title of the play, the role and the actor.
''' 
def find_actors():
    con = sqlite3.connect("teater.db")
    cur = con.cursor()
    cur.execute('''SELECT DISTINCT Teaterstykke.Tittel, Ansatt.Navn, Rolle.Navn 
                FROM Teaterstykke JOIN PaaAkt ON Teaterstykke.StykkeID = PaaAkt.StykkeID 
                JOIN Rolle ON PaaAkt.RolleID = Rolle.RolleID 
                JOIN SpillerRolle ON PaaAkt.RolleID = SpillerRolle.RolleID 
                JOIN Ansatt ON SpillerRolle.AnsattID = Ansatt.AnsattID''')
    for row in cur.fetchall():
        print(f"{row[0]}, Rolle: {row[2]}, Skuespiller: {row[1]}")