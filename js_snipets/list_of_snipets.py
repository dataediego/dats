Certainly! Here is a list of useful JavaScript snippets that you can use in Selenium with Python for web automation:

1. **Click on an Element:**
   - Simulate a click on a web element using JavaScript.

    ```python
    element = driver.find_element_by_css_selector('your_selector')
    driver.execute_script("arguments[0].click();", element)
    ```

2. **Scroll to Element:**
   - Scroll to bring a specific element into view.

    ```python
    element = driver.find_element_by_css_selector('your_selector')
    driver.execute_script("arguments[0].scrollIntoView();", element)
    ```

3. **Scroll to the Bottom of the Page:**
   - Scroll to the bottom of the page.

    ```python
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    ```

4. **Set Attribute Value:**
   - Set the value of an attribute for a web element.

    ```python
    element = driver.find_element_by_css_selector('your_selector')
    driver.execute_script("arguments[0].setAttribute('attribute_name', 'new_value');", element)
    ```

5. **Get Inner Text:**
   - Retrieve the inner text of a web element.

    ```python
    element = driver.find_element_by_css_selector('your_selector')
    inner_text = driver.execute_script("return arguments[0].innerText;", element)
    ```

6. **Change Page URL:**
   - Change the URL of the current page.

    ```python
    new_url = "https://example.com"
    driver.execute_script("window.location.href = arguments[0];", new_url)
    ```

7. **Disable Element:**
   - Temporarily disable a web element.

    ```python
    element = driver.find_element_by_css_selector('your_selector')
    driver.execute_script("arguments[0].disabled = true;", element)
    ```

8. **Get Browser Dimensions:**
   - Retrieve the width and height of the browser window.

    ```python
    dimensions = driver.execute_script("return [window.innerWidth, window.innerHeight];")
    ```

9. **Handle Alerts:**
   - Accept or dismiss JavaScript alerts.

    ```python
    driver.execute_script("window.alert('Hello, World!');")
    alert = driver.switch_to.alert
    alert.accept()  # or alert.dismiss()
    ```

10. **Execute Custom JavaScript:**
    - Execute any custom JavaScript code.

    ```python
    driver.execute_script("console.log('Hello from Selenium!');")
    ```

Remember to adapt these snippets based on the specific requirements and context of your web automation project.