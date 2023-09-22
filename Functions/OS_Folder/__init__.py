from .os_dir_find_software import *
from .os_dir_find_files import *
from .os_dir_print_paths import *
from .os_sys_status import *

# find_files_via_input(dir,name) , search_folder(dir,name) , get_executable_path(name), get_tree_string(dir), get_wifi_info() #


# Functions available are listed below #

# Script to find files by name/ext #
# Main function is find_files_via_input() -> input required is directory path & file name / extension #
# Return string of file paths #

# Script to find folders by name #
# Main function is search_folder() -> input required is root directory path & folder name #
# Return string of folder and its items if found #

# Script to find software by name #
# Main function is get_executable_path() -> input required is software name #
# Returns a string of software path #

# Returns a list of all the files in the directory tree at the given path #
# Main function is get_tree_string() -> input required is directory path #
# Return string of tree diagram #

# Main function is get_wifi_info() -> no input required #
# Returns a list of statuses, each status is a list of strings # X 4

# Main function is gget_battery_info() -> no input required #
# Return a string of battery status #