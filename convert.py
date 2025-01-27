import pandas as pd

# Specify the input Excel file and output CSV file
excel_file = 'cats.xlsx'  # Replace with your Excel file name
csv_file = 'cats.csv'

# Read the Excel file
try:
    df = pd.read_excel(excel_file)

    df.to_csv(csv_file, index=False)

    print(f"CSV file '{csv_file}' has been created successfully.")
except FileNotFoundError:
    print(f"Error: The file '{excel_file}' was not found.")
except Exception as e:
    print(f"An error occurred: {e}")
