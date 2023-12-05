from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Initialize the WebDriver
driver = webdriver.Chrome()

# Open a website
driver.get("https://example.com")

# Explicit wait for an element to be present
try:
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "your_element_id"))
    )
    print("Element is present on the page")
except Exception as e:
    print(f"Exception: {e}")
finally:
    # Close the browser window
    driver.quit()
