import os
import sys

def compare_ids_with_folder(id_file, folder_path, output_file):
    # Redirect stdout to both console and file
    class Logger(object):
        def __init__(self, filename="Default.log"):
            self.terminal = sys.stdout
            self.log = open(filename, "w")

        def write(self, message):
            self.terminal.write(message)
            self.log.write(message)

        def flush(self):
            self.terminal.flush()
            self.log.flush()

    sys.stdout = Logger(output_file)

    # Read IDs from the file
    with open(id_file, 'r') as file:
        ids = set(line.strip() for line in file)

    # Get list of files in the folder
    files = set(os.listdir(folder_path))

    # Find matches and mismatches
    matches = ids.intersection(files)
    ids_not_found = ids - files
    files_not_in_ids = files - ids

    # Print results
    print(f"Comparison results:")
    print(f"ID file: {id_file}")
    print(f"Folder path: {folder_path}")
    print(f"\nMatching IDs found as filenames: {len(matches)}")
    for match in matches:
        print(f"- {match}")

    print(f"\nIDs not found as filenames: {len(ids_not_found)}")
    for id_not_found in ids_not_found:
        print(f"- {id_not_found}")

    print(f"\nFiles in folder not in ID list: {len(files_not_in_ids)}")
    for file_not_in_ids in files_not_in_ids:
        print(f"- {file_not_in_ids}")

    # Reset stdout
    sys.stdout = sys.stdout.terminal

# Example usage
id_file = 'output.txt'  # The file we created in the previous script
folder_path = r"F:\downloads_sideload"  # Using raw string for Windows path
output_file = 'comparison_results.txt'  # File to save the output

compare_ids_with_folder(id_file, folder_path, output_file)
print(f"Results have been printed to the console and saved to {output_file}")