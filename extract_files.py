import os
from pathlib import Path

def get_all_files():
    print("Fetch all file paths from the entire system and save to file_list.txt.")
    system_root = "C:\\" if os.name == "nt" else "/"  # Windows: C:\, Linux: /
    output_file = "file_list.txt"

    with open(output_file, "w", encoding="utf-8") as f:
        for root, _, files in os.walk(system_root):
            for file_name in files:
                file_path = os.path.join(root, file_name)
                f.write(file_path + "\n")
    print('All file paths are extracted')

def get_files_by_extension(extension):
    """
    Reads 'file_list.txt' and filters out files based on the given extension.
    Returns a list of matching file paths.
    """
   
    with open("file_list.txt", "r", encoding="utf-8") as f:
        file_paths = f.read().splitlines()

    matching_files = [file for file in file_paths if file.lower().endswith(tuple(extension))]

    return matching_files




