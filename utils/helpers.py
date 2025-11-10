import os, time

def clear_console():
    """"Clears the console, differs based on the operating system for cross platform integration"""
    time.sleep(0.5)
    os.system('clear' if os.name == 'posix' else 'cls') 