import os

def run_script(script_name):
    script_path = os.path.join("user_stories", script_name)
    os.system(f"python {script_path}")

def main():
    print("Welcome to the User Story Runner!")


    while True:
        print("Please select a script to run:")
        print("1. brukstilfelle_4.py")
        print("2. brukstilfelle_5.py")
        print("3. brukstilfelle_6.py")
        print("4. brukstilfelle_7.py")
        print("0. Exit")
        choice = input("Enter your choice: ")
    
        if choice == "1":
            run_script("brukstilfelle_4.py")
        elif choice == "2":
            run_script("brukstilfelle_5.py")
        elif choice == "3":
            run_script("brukstilfelle_6.py")
        elif choice == "4":
            run_script("brukstilfelle_7.py")
        elif choice == "0":
            break
        else:
            print("Invalid choice. Please try again.")
        input("Press Enter to continue...")

if __name__ == "__main__":
    main()