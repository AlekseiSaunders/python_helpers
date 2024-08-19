import os
import json

def delete_files_not_in_json(folder_path, json_file_path):
    # Read the JSON file
    with open(json_file_path, 'r') as json_file:
        json_data = json.load(json_file)

    # Extract just the ID fields from the JSON data
    file_ids = [item['ID'] for item in json_data]

    # Get all files in the folder
    all_files = os.listdir(folder_path)

    # Find files to delete (files whose names don't start with any ID)
    files_to_delete = [file for file in all_files if not any(file.startswith(id) for id in file_ids)]

    # Delete files
    for file_name in files_to_delete:
        file_path = os.path.join(folder_path, file_name)
        try:
            if os.path.isfile(file_path):
                os.remove(file_path)
                print(f"Deleted: {file_name}")
            else:
                print(f"Skipped: {file_name} (not a file)")
        except Exception as e:
            print(f"Error deleting {file_name}: {str(e)}")

    print(f"Deletion complete. {len(files_to_delete)} files were processed.")

# Specific path to your folder
folder_path = r"C:\Users\WPS VRDemo048\Desktop\WildX Sideloading Files_20240417\downloads_sideload"

# Path to your JSON file
json_file_path = r"C:\Users\WPS VRDemo048\Desktop\WildX Sideloading Files_20240417\downloads_sideload\file_list.json"

delete_files_not_in_json(folder_path, json_file_path)