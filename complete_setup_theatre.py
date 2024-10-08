import os, sys, sqlite3, config
from setup.insert_seats_hovedscenen import insert_seats as insert_seats_hovedscenen
from setup.insert_seats_gamle_scene import insert_seats as insert_seats_gamle_scene


def main(db_name: str = config.DEFAULT_DB):
    arguments = sys.argv[1:]

    if len(arguments) == 0:
        arguments = [db_name]
        print(f"Bruker default '{db_name}'")

    elif len(arguments) > 1:
        print("for mange argumenter")
        print("Slik gjør du: python3 complete_setup_theatre.py <database.db>")
        return

    db = arguments[0].strip()

    teardown(db)

    print("Lager tabeller i databasen...")

    con = sqlite3.connect(db)
    cur = con.cursor()

    with open("setup/setup_tables.sql", "r") as file:
        setup_tables = file.read()
        cur.executescript(setup_tables)
        con.commit()

    print("Tabeller laget!")
    print()

    print("Setter inn data i tabellene...")

    with open("setup/insert_data.sql", "r") as file:
        insert_data = file.read()
        cur.executescript(insert_data)
        con.commit()

    print("Data satt inn!")
    print()

    con.close()

    insert_seats_hovedscenen(db)
    insert_seats_gamle_scene(db)


def teardown(db: str = config.DEFAULT_DB):
    try:
        if os.path.exists(db):
            os.remove(db)
            print(f"Slettet '{db}'")
            print()
    except FileNotFoundError:
        pass


def reset_db():
    teardown()
    main()


if __name__ == "__main__":
    main()
