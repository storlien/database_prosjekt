import os
import sys
import sqlite3
from setup.insert_seats_hovedscenen import insert_seats as insert_seats_hovedscenen
from setup.insert_seats_gamle_scene import insert_seats as insert_seats_gamle_scene

def main(db_name: str = "teater.db"):
    arguments = sys.argv[1:]

    if len(arguments) == 0:
        arguments = [db_name]
        print(f"Missing argument, using default '{db_name}'")

    elif len(arguments) > 1:
        print("Too many arguments")
        print("Usage: python3 complete_setup_theatre.py <database.db>")
        return

    db = arguments[0].strip()

    teardown(db)

    print("Creating tables in database...")

    con = sqlite3.connect(db)
    cur = con.cursor()

    with open("setup/setup_tables.sql", "r") as file:
        setup_tables = file.read()
        cur.executescript(setup_tables)
        con.commit()

    print("Successfully created tables!")
    print()

    print("Inserting data into tables...")

    with open("setup/insert_data.sql", "r") as file:
        insert_data = file.read()
        cur.executescript(insert_data)
        con.commit()

    print("Successfully inserted data!")
    print()

    con.close()

    insert_seats_hovedscenen(db)
    insert_seats_gamle_scene(db)

def teardown(db: str = "teater.db"):
    try:
        if os.path.exists(db):
            os.remove(db)
            print("Database named", db, "removed successfully")
            print()
    except FileNotFoundError:
        pass

def reset_db():
    teardown()
    main()

if __name__ == "__main__":
    main()
