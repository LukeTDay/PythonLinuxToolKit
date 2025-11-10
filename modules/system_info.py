from utils import helpers

def menu() -> None:
    while True:
        helpers.clear_console()
        print("System Info: ")
        print("CPU Usage: ")
        print("Memory Usage: ")
        print("Disk Usage: ")
        choice = input("Enter anything to return to main menu...")
        if choice:
            break 