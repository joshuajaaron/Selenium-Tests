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
    
    # Check each checkbox
    for checkbox in checkboxes:
        if not checkbox.is_selected():
            checkbox.click()
    
    # Validate that all checkboxes are checked
    all_checked = True
    for checkbox in checkboxes:
        if not checkbox.is_selected():
            all_checked = False
            break
    
    if all_checked:
        print("All checkboxes are checked.")
    else:
        print("Not all checkboxes are checked.")
    
except Exception as e:
    print(f"Exception occurred: {e}")

finally:
    # Close the WebDriver
    driver.quit()