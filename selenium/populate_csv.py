import csv
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# Initialize the WebDriver (assuming Chrome in this example)
driver = webdriver.Chrome()

# Open the website or perform any necessary setup
driver.get("https://example.com")

# Create a CSV file and write header
csv_file_path = "scraped_data.csv"
with open(csv_file_path, 'w', newline='') as csv_file:
    csv_writer = csv.writer(csv_file)
    header = ['Column1', 'Column2', 'Column3']  # Replace with your actual column names
    csv_writer.writerow(header)

# Loop over the scraping process
for i in range(5):  # Replace 5 with the number of iterations you want
    # Perform scraping and get data
    data1 = driver.find_element_by_xpath("your_xpath_for_data1").text
    data2 = driver.find_element_by_xpath("your_xpath_for_data2").text
    data3 = driver.find_element_by_xpath("your_xpath_for_data3").text

    # Append the data to the CSV file
    with open(csv_file_path, 'a', newline='') as csv_file:
        csv_writer = csv.writer(csv_file)
        row_data = [data1, data2, data3]  # Replace with your actual data
        csv_writer.writerow(row_data)

    # Perform any other actions, navigate to the next page, etc.
    # For example, clicking on a "Next" button
    next_button = driver.find_element_by_xpath("your_xpath_for_next_button")
    next_button.click()

# Close the WebDriver
driver.quit()
