# LOG REVIEW TOOLKIT

## What is this toolkit for?

The toolkit includes many scripts supporting the user to review log files for Cisco, DrayTek and Kali. I use them for my own needs, but you can download, modify and use them for your work as desire. Please feel free to use these scripts and contact me if needed!
They can run parallelly to each other including themselves, therefore you can create your own script to run them all at once (as long as your computer can handle them LOL).

## How to use them?

### Detect_abnormal_Cisco.py

> Usage

`python Detect_abnormal_Cisco.py <folder_path> <normal_code_1> <normal_code_2> ...`

In there:
- `<folder_path>` is the path to the folder of MONTH with the name format as **Cisco_Log_Feb23**
-> If your `<folder_path>` have different format, it is suggested to review *line 12* in the script
- `<normal_code_1>`, `<normal_code_2>`,... are strings considered as normal. Lines that contain these strings will be passed during the review process<br>
-> If you don't input these `<normal_code>`, the default code list will be applied. Look over *line 23* in the script for the default code list

> Result

- After the review, the summary will be printed on the console, it contains 2 information:
    1. The number of missing dates in that MONTH and the list of them
    2. The number of files containing abnormal codes and the list of them
- You missed the summary on the console? Don't worry, it also created a **Summary \<MONTH\>.txt** with the exact information in the output folder
- The folder **Cisco logs review** will be created (if not existed) in the location where you run the command, and the detail of abnormal lines will be in there for your manually further review<br>
-> You can change the result location at *line 6* in the script

### Detect_abnormal_Draytek.py

> Usage

`python Detect_abnormal_Draytek.py <folder_path> <normal_code_1> <normal_code_2> ...`

In there:
- `<folder_path>` is the path to the folder of MONTH with the name format as **Draytek_SysLog_Feb2023**<br>
-> If your `<folder_path>` have different format, it is suggested to review *line 12* in the script
- `<normal_code_1>`, `<normal_code_2>`,... are strings considered as normal. Lines that contain these strings will be passed during the review process<br>
-> If you don't input these `<normal_code>`, the default code list will be applied. Look over *line 23* in the script for the default code list

> Result

- After the review, the summary will be printed on the console, it contains 2 information:
    1. The number of missing dates in that MONTH and the list of them
    2. The number of files containing abnormal codes and the list of them
- You missed the summary on the console? Don't worry, it also created a **Summary \<MONTH\>.txt** with the exact information in the output folder
- The folder **Draytek logs review** will be created (if not existed) in the location where you run the command, and the detail of abnormal lines will be in there for your manually further review<br>
-> You can change the result location at *line 6* in the script

### Remove_strings.py

> Usage

`python Remove_strings.py <root_path> <unwanted_string_1> <unwanted_string_2> ...`

In there:
- `<root_path>` is the path of the root folder containing folders of MONTH as the example below:<br>
    \<root_path\><br>
    ├───Cisco_Log_Feb23<br>
    ├───Cisco_Log_Jan23<br>
    └───Cisco_Log_Mar23<br>
-> This script is used specially for the Cisco logs and DrayTek logs, whose each MONTH folder is **1-level folder**. Please modify the script if you want to use it for another directory tree.
- `<unwanted_string_1>`, `<unwanted_string_2>`,... are strings that need removing. Lines that contain these strings will be removed during the running process

> Result

- After the script is done, a folder **Removing strings result** with the exact directory tree of `<root_path>` but new files inside, will appear in the location where you run the command<br>
-> You can change the result location at *line 12* in the script

