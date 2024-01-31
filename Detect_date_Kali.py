from os import walk
from os.path import join
import sys

# Get root path and year
root_path = sys.argv[1]
try:
    the_year = int(sys.argv[2])
except:
    print("Please try again with the second argument as the year of logs!")
    exit()

# Prepare dates
MONTHS = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
DAYS = [31, 29 if the_year%4==0 else 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
DATES = [MONTHS[idx]+" "+f"{day:2}" for idx in range(12) for day in range(1,DAYS[idx]+1)]

def scan_file(relative_path):
    file_path = join(root_path, relative_path)

    # Read file
    with open(file_path, "r", encoding="utf-8") as file:
        try:
            lines = file.readlines()
        except:
            return      
        
    # Remove dates
    for line in lines:
        try:
            DATES.remove(line[:6])
        except:
            continue
    

def scan_folder(relative_path):
    folder_path = join(root_path, relative_path)
    
    # Get folder and file lists
    file_list, folder_list = [], []
    for (dirpath, folder_name, file_name) in walk(folder_path):
        folder_list.extend(folder_name)
        file_list.extend(file_name)
        break

    # Notification
    file_number, folder_number = len(file_list), len(folder_list)
    print("I have found " + str(folder_number) + " folders and " + str(file_number) + " files in directory " + folder_path)
    file_count = 1

    # Scan files
    for file_name in file_list:
        scan_file(join(relative_path, file_name))
        print("Done file " + str(file_count) + "/" + str(file_number), end="\r")

    # Scan folders
    for folder_name in folder_list:
        scan_folder(join(relative_path, folder_name))


scan_folder("")
print("Missing dates: " + ", ".join(DATES))
with open("Missing dates.txt", "w", encoding="utf-8") as result_file:
    result_file.write(", ".join(DATES))