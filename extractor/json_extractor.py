import json
import codecs

def extract_fields(input_file, output_file, fields):
    # Read the input JSON file with UTF-8 encoding and error handling
    with codecs.open(input_file, 'r', encoding='utf-8', errors='ignore') as f:
        data = json.load(f)
    
    # Extract the specified fields
    extracted_data = []
    if isinstance(data, list):
        extracted_data = [{field: item.get(field) for field in fields if item.get(field) is not None} for item in data]
    if isinstance(data,dict):
        extracted_data = {field: data.get(field) for field in fields if data.get(field) is not None}
        
    # Write the extracted data to the output JSON file
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(extracted_data, f, indent=2, ensure_ascii=False)

# Usage
input_file = 'metadata.json'  # Replace with your input file name
output_file = 'id_name.json'  # Replace with your desired output file name
fields_to_extract = ['ID', 'Name']

try:
    extract_fields(input_file, output_file, fields_to_extract)
    print(f"Extraction complete. Check {output_file} for results.")
except Exception as e:
    print(f"An error occurred: {str(e)}")
    print("If the error persists, please check the encoding of your input file.")