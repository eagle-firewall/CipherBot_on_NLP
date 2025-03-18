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

def get_files_by_extension(files):
    extension = files.split('.')[-1]  # Extract extension (e.g., "txt")
    first_letter = files[0].lower()   # Extract first letter (case insensitive)
    length = len(files)               # Get length of input filename

    # Read file paths from the list
    with open("file_list.txt", "r", encoding="utf-8") as f:
        file_paths = f.read().splitlines()

    # Filter files
    matching_files = [
        file for file in file_paths 
        if os.path.basename(file).lower().endswith(f".{extension.lower()}")  # Compare only filename
        and os.path.basename(file)[0].lower() == first_letter  # Check first letter
        and len(os.path.basename(file)) >= length  # Check length
    ]    
    return matching_files




