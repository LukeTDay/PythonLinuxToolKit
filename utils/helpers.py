import os, time

def clear_console(duration: float=0.5):
    """"Clears the console, differs based on the operating system for cross platform integration"""
    time.sleep(duration)
    os.system('clear' if os.name == 'posix' else 'cls') 