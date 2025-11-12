import psutil
import time
import curses
from utils import helpers
from rapidfuzz import fuzz

def print_running_processes() -> None:
    helpers.clear_console(duration=0)
    #This has to be done for CPU to be calculated correctly
    for proc in psutil.process_iter():
        proc.cpu_percent(interval=0)
        for child in proc.children():
            child.cpu_percent(interval=0)
    time.sleep(1)

    for proc in psutil.process_iter(['pid', 'name', 'status','cpu_percent']):
        print(f"NAME : {(proc.info["name"])[:30]:<30} CPU % : {proc.info["cpu_percent"]:<7.2f}% PID : {proc.info["pid"]:<10} STATUS : {proc.info["status"]:<10}")
        #print(proc.info)
        for child in proc.children():
            print(f"   NAME : {(child.name())[:27]:<27} CPU % : {child.cpu_percent():<7.2f}% PID : {child.pid:<10}")
        if proc.children():
            print()
    input("\nEnter to return...")
    return

def kill_running_process() -> None:
    helpers.clear_console()
    print(f"Kill Running Process...\n")

    process_to_kill_PID = int(input("Please enter the PID of the process you would like to kill: "))
    try:
        process_to_kill = psutil.Process(process_to_kill_PID)
    except psutil.NoSuchProcess as e:
        print(f"\nThere is no such process with the PID: {process_to_kill_PID}")
        print(f"Error: {e}")
        print(f"\nReturning to process manager in 3 seconds)")
        time.sleep(3)
        return

    helpers.clear_console()
    print(f"Name: {process_to_kill.name()}")
    print(f"PID : {process_to_kill.pid}")
    try:
        print(f"Mem : {process_to_kill.memory_percent():.2f}%")
    except psutil.AccessDenied:
        print(f"Mem : Mem could not be accessed")

    for child in process_to_kill.children():
        print(f" Child: ")
        print(f"  Name: {child.name()}")
        print(f"  PID : {child.pid}")
        try:
            print(f"  Mem : {child.memory_percent():.2f}%")
        except psutil.AccessDenied:
            print(f"  Mem : Mem could not be accessed")
    while True:
        choice : str = input(f"Are you sure you would like to end this process? 'Y' / 'N': ")
        if choice.lower() == "y":
            #Allow the program to terminate gracefully
            print(f"Sending SIG TERM")
            process_to_kill.terminate()
            process_exit_code = None
            try:
                process_exit_code = process_to_kill.wait(timeout=3)
            except psutil.TimeoutExpired:
                print(f"Sending SIG KILL")
                process_to_kill.kill()
            if process_exit_code: 
                print(f"Process terminated gracefully with exit code {process_exit_code}")
            else:
                print(f"Process was forcefully terminated")
            time.sleep(2)
            return
        elif choice.lower() == "n":
            print(f"Operation Aborted returning to menu")
            time.sleep(2)
            return
        else:
            print(f"Invalid Choice")

def search_running_processes(stdscr) -> None:
    curses.cbreak()
    stdscr.nodelay(True)
    search_stack = ""

    procs = [(p.pid, p.name()) for p in psutil.process_iter(['pid','name'])]

    while True:
        #This key is returned in unicode format
        key = stdscr.getch()
        #ord converts the character ! into unicode so it can be effectively compared
        if key == ord('!'): 
            break
        elif key == curses.KEY_BACKSPACE:
            search_stack = search_stack[:-1]
        #A -1 is returned when nothing is pressed so this captures anything that is not nothing
        elif key != -1: 
            search_stack += chr(key)

        #Fuzz
        filtered_procs = []
        for pid,name in procs:
            score = fuzz.partial_ratio(search_stack, name)
            if score > 60:
                filtered_procs.append((score,name,pid))
        filtered_procs.sort(reverse=True)

        stdscr.erase()
        stdscr.addstr(0,0,f"{"PID":6}  {"NAME"}")
        for x in range(min(10,len(filtered_procs))):
            stdscr.addstr((x+1),0,f"{((filtered_procs[x])[2]):<6}  {((filtered_procs[x])[1])}")
        stdscr.addstr(11, 0, f"Enter '!' to return to menu")
        stdscr.addstr(12, 0, f"Search: {search_stack}")
        stdscr.refresh()


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
        elif choice == "2":
            kill_running_process()
        elif choice == "3":
            curses.wrapper(search_running_processes)
        elif choice == "4":
            return
        else:
            print(f"Invalid Option.")