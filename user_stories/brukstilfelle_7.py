import sqlite3

'''

Brukstielle 7

Finds the actors that play in the same act as input actor and prints the title of the play and the actors.

'''
def actors_same_act(actor, db: str = "teater.db") -> None:
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

# Example of use:
# actors_same_act("Synnøve Fossum Eriksen")

