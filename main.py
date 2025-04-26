import pandas as pd
import os

def get_second_column_values_from_all_sheets(file_path):
    """
    Reads an Excel file and extracts all non-empty values from the second column (column B)
    across all sheets.

    Args:
        file_path (str): The full path to the Excel file (.xlsx).

    Returns:
        list: A single list containing all collected values.
    """
    # Load the whole Excel workbook (requires openpyxl for .xlsx)
    excel_file = pd.ExcelFile(file_path, engine='openpyxl')


    # We'll gather all the values into this list
    second_column_values = []

    # Go through each sheet in the workbook by name
    for sheet_name in excel_file.sheet_names:
        # Read the current sheet's data
        df = excel_file.parse(sheet_name)

        # Make sure there's actually a second column before trying to access it
        if df.shape[1] >= 2:
            # Grab column B (index 1), drop any empty cells, convert to Python list
            # Using .iloc to select by integer location (0-based index)
            values = df.iloc[:, 1].dropna().tolist()
            # Add the list of values from this sheet to our main list
            second_column_values.extend(values)

    return second_column_values

# --- Example of how to use the function ---

# Construct the full path to the target Excel file on the Desktop
# os.path.expanduser("~") gets the user's home directory path
file_path = os.path.join(os.path.expanduser("~"), "Desktop", "Worksheet", "Licensed-TVET-institutions-in-Kenya-2.xlsx")

# Call our function to process the file
values = get_second_column_values_from_all_sheets(file_path)


# --- Display the results ---

# Show the combined list collected from all sheets
print("Combined list from second columns of all sheets:")
print(values)

# Show how many values were found in total
print(f"\nTotal number of values collected: {len(values)}")