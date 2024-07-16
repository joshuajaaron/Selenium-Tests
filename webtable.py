from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Configure the Selenium WebDriver (make sure you have installed ChromeDriver and it is in your PATH)
driver = webdriver.Chrome()

# Navigate to the webpage
driver.get("https://rahulshettyacademy.com/AutomationPractice/")

try:
    # Wait for the table to be visible
    table_xpath = "/html/body/div[3]/div[2]/fieldset[2]/div[1]/table"
    table = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, table_xpath)))

    # Construct the XPath to find Joe Postman's row
    joe_postman_xpath = f"{table_xpath}/tbody/tr[td[text()='Joe'] and td[text()='Postman'] and td[text()='Chennai'] and td[text()='46']]"
    joe_postman_row = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, joe_postman_xpath)))

    # Check if the row is found
    if joe_postman_row:
        print("Found Joe Postman's row.")

        # Get the amount from the row
        amount_xpath = f"{joe_postman_xpath}/td[4]"
        amount_element = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, amount_xpath)))
        amount = amount_element.text

        # Validate the amount
        if amount == "46":
            print("Validation successful: Joe Postman is from Chennai and has an amount of 46.")
        else:
            print(f"Validation failed: Joe Postman's amount is {amount} instead of 46.")
    else:
        print("Validation failed: Joe Postman's details not found.")

except Exception as e:
    print(f"Error occurred: {str(e)}")

finally:
    # Close the browser
    driver.quit()