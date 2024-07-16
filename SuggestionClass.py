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
    
    # Type "South" into the autocomplete input field
    autocomplete_input.send_keys("South")
    
    # Wait for the autocomplete options to appear (adjust timeout as needed)
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".ui-menu-item")))
    
    # Find and click on the option that matches "South Africa"
    option = driver.find_element(By.XPATH, "//div[@class='ui-menu-item-wrapper' and text()='South Africa']")
    option.click()
    
    print("Selected 'South Africa' from autocomplete.")

except Exception as e:
    print(f"Exception occurred: {e}")

finally:
    # Close the WebDriver
    driver.quit()