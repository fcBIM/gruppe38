import pandas as pd
import numpy as np
import json


# Load the Excel file
file_path_csv = "Load path"
# Read the csv file, define that the separator in the csv file is = ; and that the language is with special characters. In our case with danish letters.
df = pd.read_csv(file_path_csv, sep=';', encoding='latin1')

# Convert the DataFrame into a matrix and then to a list
matrix = df.to_numpy().tolist()

# Convert the list to a JSON string
json_data = json.dumps(matrix, indent=4)

# Save the JSON string to a file
output_path = r"Export JSON string to file path."
with open(output_path, 'w') as json_file:
    json_file.write(json_data)

print(f"Data has been successfully written to {output_path}")
