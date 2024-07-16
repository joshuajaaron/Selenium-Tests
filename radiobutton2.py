from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Initialize Chrome WebDriver (adjust the path to your chromedriver if necessary)
driver = webdriver.Chrome()

try:
    # Open the webpage containing the radio buttons
    driver.get("https://rahulshettyacademy.com/AutomationPractice/")  # Replace with your actual URL

    # Wait for the radio buttons to be clickable
    radio_buttons = WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.XPATH, "//input[@type='radio']"))
    )

    # Click on radio button 2
    for radio_button in radio_buttons:
        if radio_button.get_attribute("value") == "option2":
            radio_button.click()
            break

    # Validate that radio button 2 is selected and no other radio button is selected
    radio_buttons_state = [radio_button.is_selected() for radio_button in radio_buttons]
    assert radio_buttons_state == [False, True, False], "Radio button 2 is not the only button selected."

    print("Radio button 2 is selected and validated.")

except Exception as e:
    print(f"Exception occurred: {e}")

finally:
    # Close the browser window
    driver.quit()