import psutil
import time
from utils import helpers
def print_running_processes() -> None:
    helpers.clear_console()
    #This has to be done for CPU to be calculated correctly
    for proc in psutil.process_iter():
        proc.cpu_percent(interval=0)
        for child in proc.children():
            child.cpu_percent(interval=0)
    time.sleep(1)
    for proc in psutil.process_iter(['pid', 'name', 'status','cpu_percent']):
        print(f"NAME : {proc.info["name"]:<50} CPU % : {proc.info["cpu_percent"]:<7.2f}% PID : {proc.info["pid"]:<10} STATUS : {proc.info["status"]:<10}")
        #print(proc.info)
        for child in proc.children():
            print(f"   CHILD : NAME : {child.name():<39} CPU % : {child.cpu_percent():<7.2f}% PID : {child.pid:<10}")
        if proc.children():
            print()
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
        elif choice == "4":
            return
        else:
            print(f"Invalid Option.")