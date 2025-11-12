from modules import system_info, process_manager, file_organizer
from utils import helpers

def print_main_menu() -> str:
    helpers.clear_console()
    print("Python Linux Toolkit")
    print("1. System Info")
    print("2. Process Manager")
    print("3. File Organizer")
    print("4. Network Tools")
    print("5. Exit")
    return input("Please enter your choice: ")

if __name__ == "__main__":
    while True:
        choice = print_main_menu()
        if choice == "1":
            system_info.menu()
        elif choice == "2":
            process_manager.menu()
        elif choice == "3":
            file_organizer.menu()
        elif choice == "4":
            #network_tools.menu()
            pass
        elif choice == "5":
            print("Goodbye")
            break
        else:
            print("Invalid option.")