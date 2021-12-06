from selenium import webdriver
from selenium.webdriver.common.by import By

import time
from selenium.webdriver.chrome.service import Service
import json
import utils
import db
from webdriver_manager.chrome import ChromeDriverManager


s = Service('C:\\Users\\ameer.hamza\\Desktop\\chromedriver.exe')

## LOGIN FUNCTIONALITY
def login(email,password):
    driver = webdriver.Chrome(service=s)
    driver.get("https://secure.indeed.com/account/login")
    job_title=driver.find_element(By.ID,"login-email-input")
    job_title.click()
    time.sleep(3)
    job_title.send_keys(email)
    job_title=driver.find_element(By.ID,"login-password-input")
    job_title.click()
    time.sleep(3)
    job_title.send_keys(password)
    time.sleep(3)
    driver.find_element(By.ID, 'login-submit-button').click()

time.sleep(4)




def scrap_all(p, title, location):
    job_links = []
    driver = webdriver.Chrome(service=s)
    user_data = driver.find_elements(By.XPATH, '//*[contains(@id,"job_")]')
    while True:
        a = str(p)
        url = 'https://au.indeed.com/' + 'jobs?q=' + title + '&' + 'l=' + location + '&start=' + a
        driver.get(url)
        user_data = driver.find_elements(By.XPATH, '//*[contains(@id,"job_")]')
        count_pages = driver.find_element(By.ID, "searchCountPages").text
        b = count_pages.split(' ')[3]
        print(b)
        time.sleep(4)
        number = b.replace(",", "")
        convert_number = int(number)
        for j in user_data:
            job_links.append(j.get_attribute('href'))
        print(job_links)
        if convert_number < len(job_links):
            print('this is convert number' , convert_number)
            print('this is lenght of job links', len(job_links))
            break
        p = p + 10

    for k in job_links:
        driver.get(k)
        company = driver.find_element(By.CLASS_NAME, 'jobsearch-DesktopStickyContainer').text
        elem = driver.find_element(By.ID, 'jobDescriptionText').text
        company.split('\n')
        print(company)
        utils.send_msg_to_db(company, elem)
        print(elem)










# driver.get(url)
# driver.maximize_window()























# title_xpath = '//*[@id="text-input-what"]'
# location_xpath = '//*[@id="text-input-where"]'
# submit_button = '//*[@id="jobsearch"]/button'

# submit_button = '//*[@id="jobsearch"]/button'


# driver.find_element(By.XPATH,title_xpath).send_keys('Electrical Engineer')
# driver.find_element(By.XPATH, location_xpath).send_keys('Sydney')

# search = driver.find_element(By.XPATH, submit_button)
# search.click()
job_ids = []
# user_data = driver.find_elements(By.XPATH, '//*[contains(@id,"job_")]')
# for i in user_data:
#     job_ids.append(i.get_attribute('herf'))
#     print(job_ids)


time.sleep(10)
# driver.close()
