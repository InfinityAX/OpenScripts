# A Python script that can check if a given executable name is running. Also works with lists.
# Credits: Alain Xu (https://github.com/InfinityAX), Traditional_Candy923 (https://www.reddit.com/user/Traditional_Candy923), Mark Rushakoff (https://stackoverflow.com/users/126042/mark-rushakoff), Mahmudul Hasan (https://stackoverflow.com/users/5571663/mahmudul-hasan)
# Version: 2.0
# NOTES:
#   - This script utilizes Microsoft's WMIC interface for WMI which has be deprecated in newer versions of Windows.
#   - This version is only for Windows and has only been tested on Windows 10 22H2 Home Edition 64-bits.
#   - The following functions do not address to potential issue where multiple executables may have the same name.
#   - The first few indexes in the output list for "os.popen('wmic process get description').read().splitlines()" are going to contain "junk" data.
#   - Consider adding checks for empty or known "bad" and duplicated inputs.


# Imports the os module needed to open, execute, and read the Windows command prompt
import os


# "os.popen('wmic process get description').read().splitlines()" creates a list of executables that are currently running using the WMIC interface for WMI through the command line
runningExecutableList = os.popen('wmic process get Name').read().splitlines()
# Due to how WMIC presents the result, some extra string processing needs to be done to remove empty strings and whitespaces
for listIndex in range(runningExecutableList.__len__()):
    runningExecutableList[listIndex] = runningExecutableList[listIndex].strip()
runningExecutableList = list(filter(("").__ne__, runningExecutableList))
print(runningExecutableList)


# Checks if the user defined executable name matches with any executables that are running
# Returns true if a match is found
# Returns false otherwise
def is_this_executable_running(executableName: str)->bool:
    runningExecutableList = os.popen('wmic process get Name').read().splitlines()
    # Due to how WMIC presents the result, some extra string processing needs to be done to remove empty strings and whitespaces
    for listIndex in range(runningExecutableList.__len__()):
        runningExecutableList[listIndex] = runningExecutableList[listIndex].strip()
    runningExecutableList = list(filter(("").__ne__, runningExecutableList))
    # Checks for matching string in the list and returns the appropriate output
    if (executableName in runningExecutableList):
        return True
    else:
        return False


# Checks if the executable names from a user defined list matches any of the ones running
# Returns list of executable names from the user defined list that are found running
def which_of_these_executables_are_running(executableNameList: list)->list:
    # "runningExecutableList" is a temporary varible made to store the list of running executes to prevent repeated calls to
    # the resource intensive "os.popen('wmic process get description').read().splitlines()" 
    runningExecutableList = os.popen('wmic process get Name').read().splitlines()
    # Due to how WMIC presents the result, some extra string processing needs to be done to remove empty strings and whitespaces
    for listIndex in range(runningExecutableList.__len__()):
        runningExecutableList[listIndex] = runningExecutableList[listIndex].strip()
    runningExecutableList = list(filter(("").__ne__, runningExecutableList))
    returnExecutableNameList = []
    
    # The following nested for loop and if statement checks if each executable name in the user defined list is running.
    # If a match is found, it gets added to the return list
    for executableName in executableNameList:
        if (executableName in runningExecutableList):
            returnExecutableNameList.append(executableName)

    return returnExecutableNameList


# Checks if all of the executable names from a user defined list are running
# Returns true if all the user defined executable names are found
# Returns false otherwise
def are_all_these_executables_running(executableNameList: list)->bool:
    runningExecutableList = os.popen('wmic process get Name').read().splitlines()
    # Due to how WMIC presents the result, some extra string processing needs to be done to remove empty strings and whitespaces
    for listIndex in range(runningExecutableList.__len__()):
        runningExecutableList[listIndex] = runningExecutableList[listIndex].strip()
    runningExecutableList = list(filter(("").__ne__, runningExecutableList))
    executableNameMatchList = []
    
    for executableName in executableNameList:
        if (executableName in runningExecutableList):
            executableNameMatchList.append(executableName)

    # The above code is mostly the same as the one used in "which_of_these_executables_are_running()"
    # Below is the additional check to see if the found executable name list matches the user defined list
    if (executableNameList == executableNameMatchList):
        return True
    else:
        return False


# Checks if at least one of the executable names from a user defined list are running
# Returns True if a match is found
# Returns false otherwise
def is_at_least_one_of_these_executables_running(executableNameList: list)->bool:
    # The code block is mostly the same as "which_of_these_executables_are_running()", but with "returnExecutableNameList" removed,
    # an immediate return True upon a match and a return False at the end
    runningExecutableList = os.popen('wmic process get Name').read().splitlines()
    # Due to how WMIC presents the result, some extra string processing needs to be done to remove empty strings and whitespaces
    for listIndex in range(runningExecutableList.__len__()):
        runningExecutableList[listIndex] = runningExecutableList[listIndex].strip()
    runningExecutableList = list(filter(("").__ne__, runningExecutableList))

    for executableName in executableNameList:
        if (executableName in runningExecutableList):
            return True
    
    return False


# Test code for debugging purposes
print(is_this_executable_running(""))
print(is_this_executable_running("r447fhgnjkrdg34247"))
print(is_this_executable_running("obs64.exe"))                          # obs64.exe is OBS Studios for 64-bit Windows
print(which_of_these_executables_are_running([]))
print(which_of_these_executables_are_running([None, 54, []]))
print(which_of_these_executables_are_running(["grdgdrg", "5645645765"]))
print(which_of_these_executables_are_running(["obs64.exe"]))
print(which_of_these_executables_are_running(["msedge.exe", "Unity Hub.exe"]))          # msedge.exe: Microsoft Edge | Unity Hub.exe: Unity Hub
print(are_all_these_executables_running([]))
print(are_all_these_executables_running([None, 54, []]))
print(are_all_these_executables_running(["grdgdrg", "5645645765"]))
print(are_all_these_executables_running(["obs64.exe"]))
print(are_all_these_executables_running(["msedge.exe", "Unity Hub.exe"]))
print(is_at_least_one_of_these_executables_running([]))
print(is_at_least_one_of_these_executables_running([None, 54, []]))
print(is_at_least_one_of_these_executables_running(["grdgdrg", "5645645765"]))
print(is_at_least_one_of_these_executables_running(["obs64.exe"]))
print(is_at_least_one_of_these_executables_running(["msedge.exe", "Unity Hub.exe"]))