import os

# Script to find software by name #
# Main function is get_executable_path() -> input required is software name #
# Returns a string of software path #

# Define a function to check if a file is executable
def is_executable(filepath):
    return os.path.isfile(filepath) and os.path.splitext(filepath)[1] == '.exe'

# Set the directory to search for executable files
directory1 = r'C:\Program Files (x86)'

directory2 = r'C:\Program Files'

# Finds all executable files in the directory #
def find_executables(directory):
    # Use os.walk to search the directory tree for all files
    executables = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            filepath = os.path.join(root, file)
            if is_executable(filepath):
                executables.append(filepath)
    return executables

# Return a list of all possible applications #
def find_all_applications():
    applications = [] # Format is [app_name, dir_no]
    dir1 = r'C:\Program Files (x86)'
    dir2 = r'C:\Program Files'
    dir3 = r'D:\SteamLibrary\steamapps\common'
    for name in os.listdir(dir1):
        applications.append([name, 1])
    for name in os.listdir(dir2):
        applications.append([name, 2])
    for name in os.listdir(dir3):
        applications.append([name, 3])
    return applications

# Return boolean for whether or not a app name exists in the list #
def is_application_in_os(app_name):
    name = app_name.lower()
    applications = find_all_applications()
    for i in range(len(applications)):
        if name == applications[i][0].lower() or name in applications[i][0].lower():
            return applications[i]
    return []

def get_executable_path(app_name):
    app = is_application_in_os(app_name)
    if app == []:
        return 'App not found'
    else:
        if app[1] == 1:
            filepath = os.path.join(r'C:\Program Files (x86)', app[0])
        elif app[1] == 2:
            filepath = os.path.join(r'C:\Program Files', app[0])
        elif app[1] == 3:
            filepath = os.path.join(r'D:\SteamLibrary\steamapps\common', app[0])
        possible_executables = find_executables(filepath)
        if len(possible_executables) == 0:
            return 'No exe found'
        else:
            count = len(possible_executables)
            result = ''
            result += str(count) + ' possible executables found' + '\n'
            for exec_path in possible_executables:
                result += exec_path + '\n'
            return result

# print(get_executable_path('steam'))