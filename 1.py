import sys

def show_menu():
    print("1. Option One")
    print("2. Option Two")
    print("3. Option Three")
    print("4. Option Four")
    print("5. Option Five")
    print("6. Exit")

def initiate(auto=False):
    while True:
        show_menu()
        if auto:
            choice = "6"   # Auto-select 'Exit' in Jenkins
            print(f"[AUTO MODE] Automatically selected: {choice}")
        else:
            choice = input("Select an option: ")

        if choice == "1":
            print("Running Option One...")
        elif choice == "2":
            print("Running Option Two...")
        elif choice == "3":
            print("Running Option Three...")
        elif choice == "4":
            print("Running Option Four...")
        elif choice == "5":
            print("Running Option Five...")
        elif choice == "6":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    # Detect if running in Jenkins or with '--auto' flag
    if "--auto" in sys.argv or not sys.stdin.isatty():
        initiate(auto=True)
    else:
        initiate(auto=False)
