from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Set up WebDriver (assuming Chrome WebDriver)
driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")

try:
    # Find the autocomplete input field by ID
    autocomplete_input = driver.find_element(By.ID, "autocomplete")
    
    # Clear any existing text in the autocomplete input field
    autocomplete_input.clear()
    
    # Type "Republic" into the autocomplete input field
    autocomplete_input.send_keys("Republic")
    
    # Wait for the autocomplete options to appear (adjust timeout as needed)
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".ui-menu-item")))
    
    # Find and click on the first option from the autocomplete list
    first_option = driver.find_element(By.CSS_SELECTOR, ".ui-menu-item")
    first_option.click()
    
    print("Selected the first option from autocomplete.")

except Exception as e:
    print(f"Exception occurred: {e}")

finally:
    # Close the WebDriver
    driver.quit()