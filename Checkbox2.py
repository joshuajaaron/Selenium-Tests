from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Set up WebDriver (assuming Chrome WebDriver)
driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")

try:
    # Find the fieldset containing the checkboxes
    fieldset = driver.find_element(By.XPATH, "//div[@id='checkbox-example']//fieldset")
    
    # Find all checkbox input elements within the fieldset
    checkboxes = fieldset.find_elements(By.XPATH, ".//input[@type='checkbox']")
    
    # Uncheck the first checkbox (index 0 in Python list)
    checkboxes[0].click()
    
    # Validate that the other checkboxes remain unchecked
    other_checkboxes_unchecked = True
    for checkbox in checkboxes[1:]:
        if checkbox.is_selected():
            other_checkboxes_unchecked = False
            break
    
    if other_checkboxes_unchecked:
        print("The other checkboxes remain unchecked.")
    else:
        print("One or more of the other checkboxes are still checked.")
    
except Exception as e:
    print(f"Exception occurred: {e}")

finally:
    # Close the WebDriver
    driver.quit()