import psutil
import platform
from utils import helpers

def get_cpu_usage() -> float:
    return psutil.cpu_percent(interval=0.1)

def get_memory_usage() -> dict[str,float]:
    mem = psutil.virtual_memory()
    return {
        "total_mb" : mem.total / (1024 ** 2),
        "used_mb"  : mem.used / (1024 ** 2),
        "percent"  : mem.percent
    }

def get_disk_usage(path: str = '/') -> dict[str,float]:
    disk = psutil.disk_usage(path)
    return {
        "total_gb": disk.total / (1024 ** 3),
        "used_gb": disk.used / (1024 ** 3),
        "free_gb": disk.free / (1024 ** 3),
        "percent": disk.percent
    }

def menu() -> None:
    while True:
        helpers.clear_console()
        print("System Info: ")
        #OS Info
        print()
        print(f"OS: {platform.system()} {platform.release()}")

        #CPU
        print()
        print(f"CPU Usage: {get_cpu_usage()}%")

        #Memory 
        print()
        mem = get_memory_usage()
        print(f"Used Memory: {mem["used_mb"]:.2f} MB")
        print(f"Total Memory: {mem["total_mb"]:.2f} MB")
        print(f"Memory Usage: {mem["percent"]}%")

        #Disk
        print()
        disk = get_disk_usage()
        print(f"Free Disk Space: {disk["free_gb"]:.2f} GB")
        print(f"Used Disk Space: {disk["used_gb"]:.2f} GB")
        print(f"Total Disk Space: {disk["total_gb"]:.2f} GB")
        print(f"Percent Disk Space Used: {disk["percent"]:.2f}")
        
        choice = input("Enter anything to return to main menu...")
        if choice:
            break 