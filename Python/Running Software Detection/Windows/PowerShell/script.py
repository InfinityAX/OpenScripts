# !!! WORK IN PROGRESS !!!

# A Python script that can check if a given executable is running. Also works with lists.
# Credits: Alain Xu (https://github.com/InfinityAX), Traditional_Candy923 (https://www.reddit.com/user/Traditional_Candy923)
# Version: 0.0
# NOTES:
#   - This script utilizes the WMI PowerShell Cmdlets through the command prompt.
#   - This version is only for Windows and has only been tested on Windows 10 22H2 Home Edition 64-bits.
#   - The following functions do not address to potential issue where multiple software may have the same executable name.
#   - The first few indexes in the output list for get_running_program_list() are going to contain "junk" data.
#   - Consider adding checks for empty or known "bad" inputs.


# Imports the os module needed to open, execute, and read the Windows command prompt
import os


# "os.popen('wmic process get description').read().split()" gets a list of currently running program
# Returns list of running program
print(os.popen('wmic process get description').read().split())


# Checks if the user defined program is running
# Returns true if the program is running
# Returns false otherwise
def is_program_running(programExecutable: str)->bool:
    # Checks for matching string in the list and returns the appropriate output
    if (programExecutable in get_running_program_list()):
        return True
    else:
        return False


# Checks if the program are running from a user defined list
# Returns list of user defined program that are running
def are_program_running (programExecutableList: list)->list:
    returnExecutableList = []
    
    # The following nested for loops and if statements checks if each program in the user defined list
    # is running. If the program is running and has not been added to the return list, it gets added to
    # the return list
    for userProgram in programExecutableList:
        for runningProgram in os.popen('wmic process get description').read().split():
            if (userProgram == runningProgram):
                if (userProgram not in returnExecutableList):
                    returnExecutableList.append(userProgram)
    
    return returnExecutableList


# Checks if all of the program are running from a user defined list
# Returns true if all of the user defined program are running
# Returns false otherwise
def are_all_program_running (programExecutableList: list)->bool:
    # Checks if the user defined program list matches the return list from are_program_running() function
    if (programExecutableList == are_program_running(programExecutableList)):
        return True
    else:
        return False


# Test code for debugging purposes
print(get_running_program_list())
print(is_program_running(""))
print(is_program_running("r447fhgnjkrdg34247"))
print(is_program_running("obs64.exe"))                          # obs64.exe is OBS Studios for 64-bit Windows
print(are_program_running([]))
print(are_program_running([None, 54, []]))
print(are_program_running(["grdgdrg", "5645645765"]))
print(are_program_running(["obs64.exe"]))
print(are_program_running(["msedge.exe", "Code.exe"]))          # msedge.exe: Microsoft Edge | Code.exe: Visual Studio Code
print(are_all_program_running([]))
print(are_all_program_running([None, 54, []]))
print(are_all_program_running(["grdgdrg", "5645645765"]))
print(are_all_program_running(["obs64.exe"]))
print(are_all_program_running(["msedge.exe", "Code.exe"]))