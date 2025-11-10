import psutil
from utils import helpers
def print_running_processes() -> None:
    helpers.clear_console()
    for proc in psutil.process_iter(['pid', 'name', 'status']):
        print(f"NAME : {proc.info["name"]:<50} PID : {proc.info["pid"]:<10} STATUS : {proc.info["status"]:<10}")
    input("\nEnter to return...")
    return


def menu() -> None:
    while True:
        helpers.clear_console()
        print(f"Process Manager")
        print()
        print(f"1. List all running processes")
        print(f"2. Kill a process by PID")
        print(f"3. Search for a process")
        print(f"4. Back to main menu")
        choice = input("Please enter your choice: ")
        if choice == "1":
            print_running_processes()
            pass
        elif choice == "4":
            return
        else:
            print(f"Invalid Option.")