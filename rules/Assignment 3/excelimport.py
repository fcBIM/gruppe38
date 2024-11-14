import pandas as pd

# Load the Excel file
file_path_xl = "C:\\Users\\kaspe\\OneDrive\\Skrivebord\\DTU\\3. semester\\41934 - Advanced BIM\\Excel_EPD_Data.xlsx" #Insert the correct file path 
df = pd.read_excel(file_path_xl)

# Convert the DataFrame into a matrix (NumPy array)
matrix = df.to_numpy()

# Print the resulting matrix
print(matrix)

