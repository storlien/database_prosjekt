import os

def run_script(script_name):
    script_path = os.path.join("user_stories", script_name)
    os.system(f"python {script_path}")

def main():
    print("Velkommen til teaterdatabasen!")


    while True:
        print("Velg et script å kjøre:")
        print("3 - Brukstilfelle 3; kjøp billett til forestilling")
        print("4 - Brukstilfelle 4; alle forestillinger og antall billetter solgt for en gitt dato")
        print("5 - Brukstilfelle 5; alle skuespillere og rollene de spiller i stykkene")
        print("6 - Brukstilfelle 6; alle forestillinger og antall billetter solgt for hver forestilling")
        print("7 - Brukstilfelle 7; alle skuespillere som spiller i samme akt som en gitt skuespiller")
        print("0 - Exit")
        choice = input("Skriv inn valget ditt:")
    
        if choice == "3":
            run_script("brukstilfelle_3.py")
        elif choice == "4":
            run_script("brukstilfelle_4.py")
        elif choice == "5":
            run_script("brukstilfelle_5.py")
        elif choice == "6":
            run_script("brukstilfelle_6.py")
        elif choice == "7":
            run_script("brukstilfelle_7.py")
        elif choice == "0":
            break
        else:
            print("Ikke-gyldig valg. Prøv igjen.")
        input("Trykk enter for å fortsette.")

if __name__ == "__main__":
    main()