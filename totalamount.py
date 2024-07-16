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

    # Find all amount elements in the table
    amount_elements_xpath = f"{table_xpath}/tbody/tr/td[4]"
    amount_elements = WebDriverWait(driver, 10).until(EC.visibility_of_all_elements_located((By.XPATH, amount_elements_xpath)))

    total_amount = 0

    # Calculate the total amount collected
    for amount_element in amount_elements:
        amount = int(amount_element.text)
        total_amount += amount

    # Validate the total amount collected
    if total_amount == 296:
        print("Validation successful: Total amount collected is 296.")
    else:
        print(f"Validation failed: Total amount collected is {total_amount} instead of 296.")

except Exception as e:
    print(f"Error occurred: {str(e)}")

finally:
    # Close the browser
    driver.quit()