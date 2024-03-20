import sqlite3

'''

Brukstilfelle 5

Finds all actors and the roles they play in the plays and prints the title of the play, the actor and the role.

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
        print(f"Stykke: {row[0]} \nSkuespiller: {row[1]} \nRolle: {row[2]}")
        print("-")
        
    con.close()
  
# Example of use: 
# find_actors()