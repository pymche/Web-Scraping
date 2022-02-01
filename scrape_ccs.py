import selenium
import time
import numpy as np
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import csv
import os
import pandas as pd

codes= {'Flexible Resource Pool - Staff Bank': 'RM6158',
'Non Clinical Temporary and Fixed Term Staff': 'RM6160',
'Permanent Recruitment Solutions': 'RM6002', 
'Provision of Clinical and Healthcare Staffing': 'RM6161', 
'Supply Teachers and Temporary Staff in Educational Establishments': 'RM3826',
'Workforce Management': 'RM1072'}

names = []

for framework, code in codes.items():
    url= 'https://www.crowncommercial.gov.uk/suppliers/search/1?search=true&framework=' + code + '&limit=400'

    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get(url)

    time.sleep(5)

    
    driver.maximize_window()

    time.sleep(5)

    try:

        driver.execute_script("window.scrollTo(0, document.body.scrollHeight*0.1);")
        time.sleep(np.random.uniform(0.5, 5))
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight*0.2);")
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight*0.3);")
        time.sleep(np.random.uniform(0.5, 5))
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight*0.45);")
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight*0.6);")
        time.sleep(np.random.uniform(1.5, 5))
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight*0.75);")
        time.sleep(np.random.uniform(0.5, 5))
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight*0.9);")
        time.sleep(np.random.uniform(0.5, 5))
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(2)

        companies = driver.find_elements(By.XPATH, "//h3[@class='govuk-heading-m ccs-heading-link ccs-font-weight-semibold govuk-!-font-size-22']")

        for company in companies:
            company = company.text
            if company == '':
                break
            else:
                print(company, ', ', framework)
            names.append([company, framework])

    except Exception as ex:
        print(ex)
        driver.quit()

# names.extend(name)


# write to csv file

with open('css_companies.csv', 'w', newline='') as csv_file:
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow(['Company name', 'Framework'])
    for line in names:
        csv_writer.writerow(line)
