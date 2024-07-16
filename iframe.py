from selenium import webdriver
from selenium.webdriver.common.by import By

# Initialize Chrome WebDriver (adjust the path to your chromedriver if necessary)
driver = webdriver.Chrome()

try:
    # Open the webpage
    driver.get("https://rahulshettyacademy.com/AutomationPractice/")  # Replace with your actual URL

    # Find the <iframe> element using XPATH starting from /html/body
    iframe_element = driver.find_element(By.XPATH, "/html/body//iframe")

    # If the element is found, print success message
    if iframe_element:
        print("Validation passed: The page contains an iframe.")
    else:
        print("Validation failed: The page does not contain an iframe.")

except Exception as e:
    print(f"Exception occurred: {e}")

finally:
    # Close the browser window
    driver.quit()