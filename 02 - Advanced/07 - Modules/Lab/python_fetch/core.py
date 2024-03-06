import getpass
import multiprocessing
import os
import platform


def generate_system_info() -> dict[str, str]:
    return {
        "System": platform.system(),
        "Machine Type": platform.machine(),
        "Number of CPU threads": str(multiprocessing.cpu_count()),
        "Python Version": platform.python_version(),
        "User Name": getpass.getuser(),
        "Current Working Directory": os.getcwd(),
    }
