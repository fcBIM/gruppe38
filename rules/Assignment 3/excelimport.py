import pandas as pd
import numpy as np
import json as json


# Load the Excel file
file_path_xl = "C:\\Users\\kaspe\\OneDrive\\Skrivebord\\DTU\\3. semester\\41934 - Advanced BIM\\Excel_EPD_Data.xlsx" #Insert the correct file path 
df = pd.read_excel(file_path_xl)

# Convert the DataFrame into a matrix (NumPy array) and then to a list
matrix = df.to_numpy().tolist()

# Convert the list to a JSON string
json_data = json.dumps(matrix, indent=4)

# Save the JSON string to a file
output_path = r"C:\Users\kaspe\OneDrive\Skrivebord\DTU\3. semester\41934 - Advanced BIM\Excel_EPD_Data.json"
with open(output_path, 'w') as json_file:
    json_file.write(json_data)

print(f"Data has been successfully written to {output_path}")
