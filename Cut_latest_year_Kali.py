from os import walk, mkdir, getcwd
from os.path import join, exists
from functools import reduce
import sys

# Get the root path
root_path = sys.argv[1]
print("\nRoot path: "  + root_path)

# Create the cut path
cut_path = join(getcwd(),"Cut latest year result")
print("Result path: " + cut_path)
if not exists(cut_path):
    mkdir(cut_path)

# Prepare special file lists
unread_files = []
unformat_files = []

MONTHS = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

def scan_file(relative_path):

    # Get the file contents
    with open(join(root_path, relative_path), "r", encoding="utf-8") as file:
        try:
            lines = file.readlines()[::-1]
        except:
            unread_files.append(relative_path)
            return
        
    if not lines:
        return

    # Cut-off the unwanted lines
    month_lines = [line[:3] for line in lines]
    if reduce(lambda x, y: x and y not in MONTHS, month_lines, True):
        unformat_files.append(relative_path)
    else:
        cut_point = len(lines)
        for idx in range(len(lines)-1):
            try: 
                if MONTHS.index(month_lines[idx]) < MONTHS.index(month_lines[idx+1]):
                    cut_point = idx+1
                    break
            except:
                continue
        lines = lines[:cut_point][::-1]

    # Write new file
    if lines:
        with open(join(cut_path, relative_path), "w", encoding="utf-8") as file:
            file.writelines(lines)

def scan_folder(relative_path):

    # Create the cut folder
    if not exists(join(cut_path, relative_path)):
        mkdir(join(cut_path, relative_path))
    
    # Get the folders and files
    file_list, folder_list = [], []
    for (dirpath, folder_name, file_name) in walk(join(root_path, relative_path)):
        folder_list.extend(folder_name)
        file_list.extend(file_name)
        break
    print("I have found " + str(len(folder_list)) + " folders and " + str(len(file_list)) + " files in directory " + join(root_path, relative_path))
    
    # Check each file
    file_count = 1
    for file_name in file_list:
        scan_file(join(relative_path, file_name))
        print("Done file " + str(file_count) + "/" + str(len(file_list)), end="\r")

    # Check each folder
    for folder_name in folder_list:
        scan_folder(join(relative_path, folder_name))

scan_folder("")

# Print out unread files
print("\nSummary:")
summary_file = open(join(cut_path, "Special files.txt"), "w", encoding="utf-8")

statement = "There are " + str(len(unread_files)) + " files that I cannot read the content:\n" + "\n".join(unread_files) + "\n"
print(statement, end="")
summary_file.write(statement)

statement = "There are " + str(len(unformat_files)) + " files that don't have regular format:\n" + "\n".join(unformat_files) + "\n"
print(statement, end="")
summary_file.write(statement)

summary_file.close()