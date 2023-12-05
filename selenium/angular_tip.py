from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Specify the path to GeckoDriver (or ChromeDriver for Chrome)
driver_path = "/path/to/geckodriver"

# Create a Firefox WebDriver instance
driver = webdriver.Firefox(executable_path=driver_path)

# Navigate to an Angular webpage
driver.get("https://example.com")

# Define a WebDriverWait with a timeout (e.g., 10 seconds)
wait = WebDriverWait(driver, 10)

# Wait for an Angular element to be present using the Angular-specific class
angular_element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "ng-scope")))

# Perform actions on the Angular element
angular_element.click()

# Close the browser window
driver.quit()
