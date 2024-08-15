# A Python script that can check if a given process name is running. Also works with lists.
# Credits: Alain Xu (https://github.com/InfinityAX), Traditional_Candy923 (https://www.reddit.com/user/Traditional_Candy923), SimonS (https://superuser.com/users/458113/simons), Alex_P (https://stackoverflow.com/users/10294689/alex-p)
# Version: 0.0
# NOTES:
#   - This script utilizes the WMI PowerShell Cmdlets through the command prompt. This will only work if you have a Windows version with PowerShell.
#   - This version is only for Windows and has only been tested on Windows 10 22H2 Home Edition 64-bits.
#   - The following functions do not address to potential issue where multiple programs may have the same process name.
#   - Consider adding checks for empty or known "bad" and duplicated inputs.


# Imports the os module needed to open, execute, and read the Windows command prompt
import os


# "os.popen('powershell -command "(Get-Process *).Name"').read().splitlines()" gets a list of currently running processes by running on of the WMI PowerShell Cmdlets commands in PowerShell through the command line
print(os.popen('powershell -command "(Get-Process *).Name"').read().splitlines())


# Checks if the user defined process name is running
# Returns true if a match is found
# Returns false otherwise
def is_this_process_running(processName: str)->bool:
    # Checks for matching string in the list and returns the appropriate output
    if (processName in os.popen('powershell -command "(Get-Process *).Name"').read().splitlines()):
        return True
    else:
        return False


# Checks if the process names from a user defined list are running
# Returns list of user defined process names that have been found
def which_of_these_processes_are_running(processNameList: list)->list:
    # "runningProcessList" is a temporary varible made to store the list of running executes to prevent repeated calls to
    # the resource intensive "os.popen('powershell -command "(Get-Process *).Name"').read().splitlines()" 
    runningProcessList = os.popen('powershell -command "(Get-Process *).Name"').read().splitlines()
    returnProcessNameList = []
    
    # The following nested for loop and if statement checks if each process name in the user defined list is running.
    # If a match is found, it gets added to the return list
    for processName in processNameList:
        if (processName in runningProcessList):
            returnProcessNameList.append(processName)
    
    return returnProcessNameList


# Checks if all of the process names from a user defined list are running
# Returns true if all of the user defined process names are found
# Returns false otherwise
def are_all_these_processes_running (processNameList: list)->bool:
    runningProcessList = os.popen('powershell -command "(Get-Process *).Name"').read().splitlines()
    processNameMatchList = []
    
    for processName in processNameList:
        if (processName in runningProcessList):
            processNameMatchList.append(processName)

    # The above code is mostly the same as the one used in "which_of_these_processes_are_running()"
    # Below is the additional check to see if the found process name list matches the user defined list
    if (processNameList == processNameMatchList):
        return True
    else:
        return False


# Checks if at least one of the process names from a user defined list are running
# Returns True if a match is found
# Returns false otherwise
def is_at_least_one_of_these_processes_running(processNameList: list)->bool:
    # The code block is mostly the same as "which_of_these_processes_are_running()", but with "returnProcessNameList" removed,
    # an immediate return True upon a match and a return False at the end
    runningProcessList = os.popen('powershell -command "(Get-Process *).Name"').read().splitlines()

    for processName in processNameList:
        if (processName in runningProcessList):
            return True
    
    return False


# Test code for debugging purposes
print(is_this_process_running(""))
print(is_this_process_running("r447fhgnjkrdg34247"))
print(is_this_process_running("obs64"))                          # obs64 is OBS Studios for 64-bit Windows
print(which_of_these_processes_are_running([]))
print(which_of_these_processes_are_running([None, 54, []]))
print(which_of_these_processes_are_running(["grdgdrg", "5645645765"]))
print(which_of_these_processes_are_running(["obs64"]))
print(which_of_these_processes_are_running(["msedge", "Unity Hub"]))          # msedge: Microsoft Edge | Unity Hub: Unity Hub
print(are_all_these_processes_running([]))
print(are_all_these_processes_running([None, 54, []]))
print(are_all_these_processes_running(["grdgdrg", "5645645765"]))
print(are_all_these_processes_running(["obs64"]))
print(are_all_these_processes_running(["msedge", "Unity Hub"]))
print(is_at_least_one_of_these_processes_running([]))
print(is_at_least_one_of_these_processes_running([None, 54, []]))
print(is_at_least_one_of_these_processes_running(["grdgdrg", "5645645765"]))
print(is_at_least_one_of_these_processes_running(["obs64"]))
print(is_at_least_one_of_these_processes_running(["msedge", "Unity Hub"]))