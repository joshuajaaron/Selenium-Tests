from selenium import webdriver
from selenium.webdriver.common.by import By

# Initialize WebDriver
driver = webdriver.Chrome()

# Open the webpage
driver.get("https://rahulshettyacademy.com/AutomationPractice/")

try:
    # Locate the radio button element
    #radio_button = driver.find_element(By.ID, "radio-btn-example")
    radio_button = driver.find_element (By.NAME, "radioButton")

    # Click on the radio button
    radio_button.click()

    # Check if the radio button is selected
    if radio_button.is_selected():
        print("Radio button selected successfully")
    else:
        print("Radio button selection failed")

    # Example of validation check
    validation_message = driver.find_element(By.ID, 'validation_message_id').text
    assert "Please select an option" in validation_message, "Validation message not as expected"

finally:
    # Quit the WebDriver
    driver.quit()
