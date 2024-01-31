from os import listdir, mkdir
from os.path import join, isdir, exists
from functools import reduce
import sys

# Get the root path
root_path = sys.argv[1]
folder_list = [folder for folder in listdir(root_path) if isdir(join(root_path,folder))]
print("\nRoot path: "  + root_path)

# Create the result path
result_path = join(root_path, "Result")
print("Result path: " + result_path)
if not exists(result_path):
    mkdir(result_path)

# Get the unwanted strings
strings = sys.argv[2:]
if not strings:
    print("You input no unwanted string, I quit!")
    exit()
print("Unwanted strings: " + ", ".join(strings))

# Folder count
folder_number = len(folder_list)
folder_count = 1

# Check each foler
for folder in folder_list:
    file_list = [file for file in listdir(join(root_path,folder))]

    # Create result folders
    if not exists(join(result_path, folder)):
        mkdir(join(result_path, folder))

    # File count
    file_number = len(file_list)
    file_count = 1
    
    # Check each file
    for file_name in file_list:

        # Read
        with open(join(root_path, folder, file_name), "r", encoding="utf-8") as file:
            lines = file.readlines()
        
        # Over-write
        with open(join(result_path, folder, file_name), "w", encoding="utf-8") as file:
            file.writelines([line for line in lines if not reduce(lambda x, y: x or y in line, strings, False)])

        # Update notification
        print("                                 ", end="\r")
        print("Folder " + str(folder_count) + "/" + str(folder_number) + ": File " + str(file_count) + "/" + str(file_number), end="\r")
        file_count += 1

    folder_count += 1

print("Done removing the unwanted strings!")