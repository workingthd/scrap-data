from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import json
f=open('user.json')
data=json.load(f)
email=data[0]['Email']
print(email)


# s = Service('C:\\Users\\muhammad.hamza\\Downloads\\chromedriver_win32\\chromedriver.exe')
# driver = webdriver.Chrome(service=s)
def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.



# driver.get("https://secure.indeed.com/account/login")
#
# job_title=driver.find_element(By.ID,"login-email-input")
# job_title.click()
# job_title.send_keys('muhammad.hamza@thdinfinity.com')
# job_title=driver.find_element(By.ID,"login-password-input")
# job_title.click()
# job_title.send_keys('ComputerScience123')
# driver.find_element(By.ID, 'login-submit-button').click()
# # driver.close()