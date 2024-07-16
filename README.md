# Selenium-Tests
Livescore assesment


Description:
This project consists of automated testing using Selenium with scripts coded using Python
These scripts can be executed locally provided you have selenium web driver installed

Installation: 
Installing Python Bindings for Selenium
Using pip, you can install selenium like this:

"pip3 install selenium"

For each script 
firstly initiate Selenium Webdriver:

from selenium import webdriver

then setup the webdriver :
driver = webdriver.Chrome()
driver.get(insert target URL for webpage here)
example:
driver.get("https://rahulshettyacademy.com/AutomationPractice/")

obtain target function to be tested and then click on "inspect" while hovering over the function/item on the webpage in order to obtain the html code for the applicable function


Example: 
/html/body/div[1]/div[1]/fieldset/legend

And Using XPATH to obtain the necessary values for the python script.




Usage: 

execute script from Local machine(terminal):
eg:

python3 totalamount.py (to calculate the total of all amounts in the total column)

This will open a Chrome web browser via Selenium web driver which will automatically perform the test and then print the output in your terminal

Output:
Successful: Validation successful: Total amount collected is 296.
Unsuccessful: Total amount collected is {total_amount} instead of 296.

or 

Error: Error occurred: {str(e)}


Contributing: 

License: Selenium used is the Open Source version -  no licence needed



