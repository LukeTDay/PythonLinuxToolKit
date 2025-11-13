from utils import helpers

def active_connections() -> None:
    return

def menu() -> None:
    while True:
        helpers.clear_console()
        print(f"Network Tools")
        print()
        print(f"1. List active connections")
        print(f"5. Exit to main menu")
        choice = input("Please enter your choice: ")
        if choice == "1":
            active_connections()
        elif choice == "5":
            #Return to the main menu
            return
        else: 
            print(f"Invalid Option")
        


    return