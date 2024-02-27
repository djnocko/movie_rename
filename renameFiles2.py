# The Script will rename filenames like this:
# 1. Filename_One_2020.* --> Filename One (2020).*
# 2. Filename Two 2020.* --> Filename Two (2020).*

import os
import re

def rename_files(folder_path):
    file_list = os.listdir(folder_path)
    pattern = r'^(.*?)\.?(\d{4})\.?(?:\d{4}p)?.*?\..*?$'

    for filename in file_list:
        match = re.search(pattern, filename)
        if match:
            name_part = match.group(1).replace(".", " ").strip()
            year_part = match.group(2)
            _, extension = os.path.splitext(filename)
            new_name = f"{name_part} ({year_part}){extension}"

            print(f"Renaming '{filename}' to '{new_name}'")
            old_path = os.path.join(folder_path, filename)
            new_path = os.path.join(folder_path, new_name)
            os.rename(old_path, new_path)

if __name__ == "__main__":
    #folder_path = r"\\IP-ADDRESS\videos\converted"
    folder_path = r"C:\Users\USERNAME\Documents\videos"
    rename_files(folder_path)