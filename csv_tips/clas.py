Certainly! Below is an example of a Python class that provides eight functions to deal with CSV files. This class uses the `csv` module for reading and writing CSV files.

```python
import csv

class CSVHandler:
    def __init__(self, filename):
        self.filename = filename

    def read_csv(self):
        """Read the content of the CSV file."""
        data = []
        with open(self.filename, 'r', newline='') as file:
            reader = csv.reader(file)
            for row in reader:
                data.append(row)
        return data

    def write_csv(self, data):
        """Write data to the CSV file."""
        with open(self.filename, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(data)

    def append_row(self, row):
        """Append a single row to the CSV file."""
        with open(self.filename, 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(row)

    def get_header(self):
        """Get the header of the CSV file."""
        with open(self.filename, 'r', newline='') as file:
            reader = csv.reader(file)
            header = next(reader, None)
        return header

    def filter_rows(self, condition_func):
        """Filter rows based on a condition function."""
        data = self.read_csv()
        filtered_data = [row for row in data if condition_func(row)]
        return filtered_data

    def sort_rows(self, key_func):
        """Sort rows based on a key function."""
        data = self.read_csv()
        sorted_data = sorted(data, key=key_func)
        return sorted_data

    def count_rows(self):
        """Count the number of rows in the CSV file."""
        data = self.read_csv()
        return len(data)

    def get_column(self, column_index):
        """Get a specific column from the CSV file."""
        data = self.read_csv()
        column = [row[column_index] for row in data]
        return column

# Example usage:
# csv_handler = CSVHandler('example.csv')
# data = csv_handler.read_csv()
# print(data)
# ... (use other methods as needed)
```

This class, `CSVHandler`, provides basic functionality for reading and writing CSV files. You can create an instance of this class, specify the filename, and then use its methods to perform various operations on the CSV file, such as reading, writing, appending rows, getting headers, filtering rows based on conditions, sorting rows, counting rows, and extracting specific columns. Adjust the methods as needed based on your specific requirements.