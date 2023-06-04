import json
import os

# Input folder path
input_folder = 'input'
# Output folder path
output_folder = 'output'

# Read the contents of the first JSON file
input_file1 = os.path.join(input_folder, 'file1.json')
with open(input_file1, 'r') as file:
    json_data1 = file.read()

# Read the contents of the second JSON file
input_file2 = os.path.join(input_folder, 'file2.json')
with open(input_file2, 'r') as file:
    json_data2 = file.read()

# Parse the JSON data into lists
data1 = json.loads(json_data1)
data2 = json.loads(json_data2)

# Merge the lists
merged_data = data1 + data2

# Convert the merged data back into a JSON string
merged_json = json.dumps(merged_data, indent=4)

# Output file path
output_file = os.path.join(output_folder, 'merged.json')

# Write the merged JSON string into the output file
os.makedirs(output_folder, exist_ok=True)
with open(output_file, 'w') as file:
    file.write(merged_json)
