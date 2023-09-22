import os

# Script to find files by name/ext #
# Main function is find_files_via_input() -> input required is directory path & file name / extension #
# Return string of file paths #

# Script to find folders by name #
# Main function is search_folder() -> input required is root directory path & folder name #
# Return string of folder and its items if found #

# Find Folder #
def search_folder(root_dir, folder_name):
    if root_dir == None:
        root_dir = os.getcwd()
    # Search for the folder within the root directory
    for item in os.listdir(root_dir):
        item_path = os.path.join(root_dir, item)
        if os.path.isdir(item_path) and item == folder_name:
            # If the folder is found, list its contents
            result = ''
            result += f"Contents of {item_path}:" + '\n'
            for subitem in os.listdir(item_path):
                result += subitem + '\n'
            return result
        elif os.path.isdir(item_path):
            # If the item is a directory, recursively search it for the folder
            search_folder(item_path, folder_name)
    # If the folder is not found, return False
    return 'Folder not found'

# # Define the folder name to search for
# folder_name = 'Sprites'

# # Get the current directory
# current_dir = os.getcwd()

# # Search for the folder within the current directory and its subdirectories
# print(search_folder( current_dir, folder_name ))


# Find Files #

def find_files_via_ext(directory, extension):
    file_list = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(extension):
                file_list.append(os.path.join(root, file))
    return file_list

def find_files_via_name(directory, filename):
    file_list = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file == filename:
                file_list.append(os.path.join(root, file))
    return file_list

def consolidate_matched_files(matching_files):
    count = len(matching_files)
    returnString = ''
    for file in matching_files:
        returnString += file + '\n'
    if returnString == '':
        returnString = 'No files found'
    return str(count) + ' files found \n' + returnString


def find_files_via_input(directory = None, value = ''):
    if directory == None:
        directory = r'C:\Users\Nabil\Desktop\DesktopBot'
    string_list = value.split(".")
    if len(string_list) > 2:
        print("Error: Too many arguments")
        raise Exception
    elif len(string_list) == 1:
        return consolidate_matched_files(find_files_via_name(directory, string_list[0]))
    else:
        return consolidate_matched_files(find_files_via_ext(directory, "." + string_list[1]))

# # Test Case #
# # Example usage
# directory = r'C:\Users\Nabil\Desktop\DesktopBot'
# filename = 'example.txt'
# matching_files = find_files_via_name(directory, filename)

# # Example usage
# directory = r'C:\Users\Nabil\Desktop\DesktopBot'
# extension = '.txt'
# txt_files = find_files_via_ext(directory, extension)

# a = consolidate_matched_files(matching_files)
# b = consolidate_matched_files(txt_files)
# print(a)
# print(b)

# print(find_files_via_input(directory,'.gif'))

# print(find_files_via_input(r'C:\Program Files (x86)','.exe'))