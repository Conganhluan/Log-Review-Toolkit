from os import mkdir, listdir
from os.path import join, exists
import sys

# Create the result folder
result_folder = "Cisco logs review"
if not exists(result_folder):
    mkdir(result_folder)

# Read the folder path
path = sys.argv[1]
print("\nPath: " + path)
the_month = path[-5:-2]

# Get the file list
file_list = listdir(path)
file_list_size = len(file_list)
print("There are " + str(file_list_size) + " log files total!")

# Get the normal code list
if sys.argv[2:]:
    normal_code_list = sys.argv[2:]
else:
    normal_code_list = ["%ASA-3", "%ASA-4", "%ASA-5", "%ASA-6", "%ASA-7"]
print("Normal code list (default in code): " if not sys.argv[2:] else "Normal code list: ", end='')
print(normal_code_list)

# Check precedences
if not file_list_size:
    print("The folder path have nothing!")
    exit
elif not normal_code_list:
    print("There is no normal code list!")
    exit()

# Create dates
MONTHS = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
DAYS = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
DATES = [MONTHS[idx]+" "+f"{day:2}" for idx in range(12) if MONTHS[idx]==the_month for day in range(1,DAYS[idx]+1)]

# Prepare abnormal file list
abnormal_file_list = []

# Check files in folder
for file_index in range(file_list_size):

    # Notify the process
    print("\rDoing file " + str(file_index+1) + "/" + str(file_list_size), end='')
    with open(join(path,file_list[file_index]), "r", encoding="utf-8") as file:

        # Check lines in file
        for line in file.readlines():
            
            # Check abnormal
            if not line:
                continue
            is_normal = False
            for code in normal_code_list:
                if line.find(code) != -1:
                    is_normal = True
                    break
            if not is_normal:
                with open(join(result_folder, file_list[file_index]), "a") as result_file:
                    result_file.write(line)
                if file_list[file_index] not in abnormal_file_list:
                    abnormal_file_list.append(file_list[file_index])

            # Check missing dates
            try:
                DATES.remove(line[:6])
            except:
                continue

# Summary
print("\n\nSummary:")
summary_file = open(join(result_folder, "Summary " + the_month + ".txt"), "w")

statement = "There are " + str(len(DATES)) + " missing dates: " + ', '.join(DATES)
print(statement, end="\n\n")
summary_file.write(statement + "\n\n")

statement = "There are " + str(len(abnormal_file_list)) + " files having abnormal codes: \n" + "\n".join(abnormal_file_list)
print(statement)
summary_file.write(statement)
