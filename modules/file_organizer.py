import os
import time

from utils import helpers
def determine_directory_to_clean() -> str:
    while True:
        helpers.clear_console()
        print(f"Enter 'x' to return to menu")
        desired_path = input("Enter the directory you would like to clean: ").strip()

        if desired_path == "x":
            return "x"
        
        desired_path = os.path.expanduser(desired_path)
        desired_path = os.path.abspath(desired_path)

        if os.path.exists(desired_path):
            print(f"{desired_path} exists")
        else:
            print(f"{desired_path} was invalid, try again")
            time.sleep(1)
            continue

        time.sleep(0.5)

        if os.path.isdir(desired_path):
            print(f"{desired_path} is a valid directory")
        else:
            print(f"{desired_path} is not a directory, try again")
            time.sleep(1)
            continue

        time.sleep(0.5)

        if os.access(desired_path, os.W_OK):
            print(f"{desired_path} is a writeable directory")
            return os.path.abspath(desired_path)
        else:
            print(f"{desired_path} is not writeable, try again")
            time.sleep(1)
            continue

def clean_temp_files() -> None:
    desired_path = determine_directory_to_clean()

    if desired_path == "x":
        return
    
    helpers.clear_console()
    print(f"Here are the files that could possibly be removed: \n")
    max_length : int = 0
    for root, dirs, files in os.walk(desired_path):
        name = ""
        for dir in dirs:
            file_path : str = os.path.join(root,dir)
            name : str = os.path.basename(file_path)

        for file in files:
            file_path : str = os.path.join(root,file)
            name : str = os.path.basename(file_path)
        
        if len(name) > max_length:
            max_length = len(name)

    for root, dirs, files in os.walk(desired_path):
        for dir in dirs:
            file_path : str = os.path.join(root,dir)
            name : str = os.path.basename(file_path)
            print(f"{name[:max_length]+"/":<{max_length}}")
    
        for file in files:
            file_path : str = os.path.join(root,file)
            stat_file : os.stat_result = os.stat(file_path)
            file_name : str = os.path.basename(file_path)
            last_access_time : float = stat_file.st_atime
            days_ago : float  = (time.time() - last_access_time) / 86400
            last_access_time_readable : str = time.ctime(last_access_time)
            print(f"  {file_name[:max_length]:<{max_length}} | {last_access_time_readable} | Last updated {days_ago:.2f} days ago")
        
    print()
    delete_older_than_days : float = float(input("Delete files older than ___ days\nPlease enter: "))
    helpers.clear_console()

    print(f"These are the files that would be deleted: ")
    print()

    files_to_delete = []
    for root, dirs, files in os.walk(desired_path):
        for file in files:
            file_path : str = os.path.join(root,file)
            stat_file : os.stat_result = os.stat(file_path)
            file_name : str = os.path.basename(file_path)
            last_access_time : float = stat_file.st_atime
            days_ago : float  = (time.time() - last_access_time) / 86400
            last_access_time_readable : str = time.ctime(last_access_time)
            if days_ago > delete_older_than_days:
                print(f"{file_name}")
                files_to_delete.append(file_path)
    
    #print(files_to_delete)
    while True:
        choice = input(f"\nPlease confirm deletion 'y' | 'n': ").lower()
        if choice == "y":
            for file_path in files_to_delete:
                os.remove(file_path)
            print(f"Files deleted")
            time.sleep(0.5)
            return
        elif choice == "n":
            print(f"Deletion halted")
            time.sleep(0.5)
            return
        else:
            print(f"Invalid Choice")
            time.sleep(0.5)
            continue


def menu() -> None:
    while True:
        helpers.clear_console()
        print(f"File Organizer")
        print()
        print(f"1. Clean Temporary Files")
        print(f"5. Exit to main menu")
        choice = input("Please enter your choice: ")
        if choice == "1":
            clean_temp_files()
        elif choice == "5":
            #Return to the main menu
            return
        else: 
            print(f"Invalid Option")