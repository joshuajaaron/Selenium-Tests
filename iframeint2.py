from selenium import webdriver
from selenium.webdriver.common.by import By

# Initialize Chrome WebDriver (adjust the path to your chromedriver if necessary)
driver = webdriver.Chrome()

try:
    # Open the webpage containing the iframe
    driver.get("https://rahulshettyacademy.com/AutomationPractice/")  # Replace with your actual URL

    # Switch to the iframe by finding its XPATH
    iframe_element = driver.find_element(By.XPATH, "/html/body//iframe")
    driver.switch_to.frame(iframe_element)

    # Find the element with class "icon fa fa-envelope" inside the iframe using XPATH
    envelope_icon_element = driver.find_element(By.XPATH, "//i[contains(@class, 'icon fa fa-envelope')]")

    # Get the text or any attribute from the envelope icon element
    icon_text = envelope_icon_element.get_attribute("class")

    # Print the retrieved class attribute of the envelope icon
    print("Icon Class:", icon_text)

except Exception as e:
    print(f"Exception occurred: {e}")

finally:
    # Switch back to the default content outside the iframe
    driver.switch_to.default_content()

    # Close the browser window
    driver.quit()