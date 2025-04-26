# Stadi za Maisha Task Answers

## 1. Python Task: Extract Second Column from All Sheets

The relevant steps I followed to perform above operation:

1. **Making a Home for the Project**: First up, I just went to my Desktop and created a new folder. I called it Worksheet – nice and simple. 

2. **Adding the Spreadsheet**: Then, I grabbed the Excel file I needed for this task, the Licensed-TVET-institutions-in-Kenya-2.xlsx one, and moved it right into that Worksheet folder I had just made. 

3. **Opening the Editor**: After that, I fired up Visual Studio Code (VS Code), my usual code editor. 

4. **Loading the Project**: In VS Code, I used the "File" > "Open Folder..." option and selected the Worksheet folder from my Desktop. This pulled my folder and the Excel file inside it into the VS Code sidebar, setting up my workspace. 

5. **Creating the Script File**: Right there within the project structure in VS Code, I created a new file and simply saved it as main.py. 

6. **Getting the Tools Ready**: Before I could run the script, I needed a couple of things: 
   a) I opened the terminal panel right inside VS Code.
   b) My code needed 'pandas' to handle the data easily and 'openpyxl' to specifically read the .xlsx file format. So, in the terminal, I ran `pip install pandas openpyxl` to get those tools installed for Python.

7. **Writing the Actual Code**: In main.py, I added essential imports at the top: `import pandas as pd` for spreadsheet handling and `import os` for file operations. With these tools in place, I wrote the Python code needed to open and process the Excel data as indicated on the instructions.

8. **Checking My Location**: I quickly checked the path shown in the terminal prompt. It read `C:\Users\Juan\Desktop\Worksheet>`, which was perfect – exactly where my main.py script and the Excel file were. 

9. **Running the Code**: Alright, with the code written, the libraries installed, and being in the right folder, I was ready to go I just typed `python main.py` into the terminal and hit Enter to execute the script and let it do its job.

### Solution Code Snippet
```python
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
```

## 2. Stadinet.co Account Creation Analysis

Verification code sent on my email basically to open my stadinet.co account. My Step 1 Screen shot after creating or signing up my stadinet.co account:

I can confirm that I have now filled out the Stadinet onboarding form with my information:
1. I entered my name as Juan Amuom.
2. I selected "University" as my highest education level.
3. I indicated that I am attending KCA University.
4. I selected "Male" as my gender

Now that I have completed Step 1; which included registering my account, setting a password, and receiving the verification code 010039 via Gmail I see the next step is to click the blue "Proceed" button meaning to continue or go on with the registration process.

This information I've provided will help Stadinet create my profile and customize my experience on the platform. I expect they will likely use these details to:
1. Set up my basic user profile
2. Connect me with relevant resources for University students
3. Potentially match me with other KCA University students
4. Show me content relevant to my educational background
