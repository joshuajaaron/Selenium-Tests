from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Initialize Chrome WebDriver (adjust the path to your chromedriver if necessary)
driver = webdriver.Chrome()

try:
    # Open the webpage containing the iframe
    driver.get("https://rahulshettyacademy.com/AutomationPractice/")  # Replace with your actual URL

    # Switch to the iframe by finding its XPATH
    iframe_element = driver.find_element(By.XPATH, "/html/body//iframe")
    driver.switch_to.frame(iframe_element)

    # Find the Register link inside the iframe using XPATH
    register_link = driver.find_element(By.XPATH, "//a[contains(text(), 'Register')]")

    # Click on the Register link
    register_link.click()

    # Wait for some time to see the result
    WebDriverWait(driver, 10).until(EC.title_contains("Register"))

    # Optionally, you can do further actions within the iframe

    # Print success message
    print("Clicked on Register link inside the iframe successfully.")

except Exception as e:
    print(f"Exception occurred: {e}")

finally:
    # Switch back to the default content outside the iframe
    driver.switch_to.default_content()

    # Close the browser window
    driver.quit()