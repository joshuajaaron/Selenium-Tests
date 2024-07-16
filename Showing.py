from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Set up WebDriver (assuming Chrome WebDriver)
driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")

try:
    # Click on the Show button using XPath
    show_button = driver.find_element(By.XPATH, "//input[@id='show-textbox']")
    show_button.click()
    
    # Wait for a brief moment to ensure the action has time to take effect
    driver.implicitly_wait(1)
    
    # Validate that the element is shown using XPath
    displayed_text = driver.find_element(By.XPATH, "//input[@id='displayed-text']")
    
    if displayed_text.is_displayed():
        print("Element is shown.")
    else:
        print("Element is still hidden.")
    
except Exception as e:
    print(f"Exception occurred: {e}")

finally:
    # Close the WebDriver
    driver.quit()


    
