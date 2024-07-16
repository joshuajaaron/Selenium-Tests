from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Initialize Chrome WebDriver
driver = webdriver.Chrome()

# Open the webpage
driver.get("https://rahulshettyacademy.com/AutomationPractice/")  # Replace with your actual URL

try:
    # Wait for the table to load (adjust sleep time according to your page loading time)
    time.sleep(3)
    
    # Find all the amount cells in the table body using XPATH
    amount_elements = driver.find_elements(By.XPATH, "/html/body/div[3]/div[2]/fieldset[2]/div[1]/table/tbody/tr/td[4]")
    
    # Initialize a variable to store the total sum
    total_sum = 0
    
    # Loop through each amount element, extract the text (which is the amount), and sum it up
    for amount_element in amount_elements:
        amount = amount_element.text.strip()  # Get the text and strip any extra whitespace
        total_sum += int(amount)  # Convert to integer and add to total_sum
    
    # Print the total sum
    print(f"Total amount sum: {total_sum}")
    
    # Check if the total sum matches 296
    if total_sum == 296:
        print("Validation passed: Total amount adds up to 296")
    else:
        print("Validation failed: Total amount does not add up to 296")
    
except Exception as e:
    print(f"Exception occurred: {e}")

finally:
    # Close the browser window
    driver.quit()