import json

def extract_ids(input_file, output_file):
    try:
        # Try to read the JSON file with UTF-8 encoding
        with open(input_file, 'r', encoding='utf-8') as file:
            data = json.load(file)
    except UnicodeDecodeError:
        # If UTF-8 fails, try with 'latin-1' encoding
        with open(input_file, 'r', encoding='latin-1') as file:
            data = json.load(file)
    
    # Extract IDs
    ids = []
    if isinstance(data, list):
        ids = [str(item.get('ID')) for item in data if isinstance(item, dict) and 'ID' in item]
    elif isinstance(data, dict):
        ids = [str(data.get('ID'))] if 'ID' in data else []
    
    # Write IDs to output file
    with open(output_file, 'w', encoding='utf-8') as file:
        for id in ids:
            file.write(f"{id}\n")

# Example usage
input_file = 'metadata.json'
output_file = 'output.txt'

try:
    extract_ids(input_file, output_file)
    print(f"IDs have been extracted from {input_file} and saved to {output_file}")
except Exception as e:
    print(f"An error occurred: {e}")
    print("Please check that your input file exists and contains valid JSON data.")