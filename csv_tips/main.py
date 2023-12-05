
"""
If you're experiencing scientific notation issues when converting a CSV file to Excel, it's likely due to the default behavior of Excel to automatically format large or small numbers in scientific notation. To prevent this behavior, you can take a few steps:

Format the cells in Excel:

After importing the CSV into Excel, select the column or cells containing the numbers.
Right-click and choose "Format Cells."
In the "Number" tab, select "Number" or "Text" as the category.
Click "OK" to apply the formatting.
Format the CSV file:

Before importing the CSV into Excel, you can modify the CSV file itself to force Excel to treat the values as text.
You can do this by adding a single quote (') before the numbers in the CSV file. For example:

'123456789
'0.000000001

"""                                       
                                          

import csv

data = [
    ['Column1', 'Column2', 'Column3'],
    ['123456789', '0.000000001', '987654321'],
    # Add your data here
]

csv_file_path = 'output.csv'

with open(csv_file_path, 'w', newline='') as csv_file:
    csv_writer = csv.writer(csv_file)
    csv_writer.writerows(data)
