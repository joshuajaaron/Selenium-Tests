from selenium import webdriver
from selenium.webdriver.common.by import By

# Initialize WebDriver
driver = webdriver.Chrome()

# Open the webpage
driver.get("https://rahulshettyacademy.com/AutomationPractice/")

try:
    # Find the radio button element using XPath
    radio_button = driver.find_element(By.XPATH, "//input[@name='radioButton' and @value='radio1']")

    # Validate if the radio button is selected
    if radio_button.is_selected():
        print("Radio button is selected.")
    else:
        print("Radio button is not selected.")

except Exception as e:
    print(f"Exception occurred: {e}")

finally:
    # Close the WebDriver
    driver.quit()