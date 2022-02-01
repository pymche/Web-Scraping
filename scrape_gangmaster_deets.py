import selenium
import time
import numpy as np
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains
import csv
import os
import pandas as pd

df = pd.read_csv(r"C:\Users\Melanie Cheung\Desktop\Rightcheckcode\Hunter\gangmasters_links.csv")

deets = []

for link in df['Link']:

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get(link)


    time.sleep(2)

    driver.maximize_window()


    time.sleep(5)


    try:

        time.sleep(np.random.uniform(15, 37))

        print('A')

        driver.execute_script("window.scrollTo(0, document.body.scrollHeight*0.1);")
        time.sleep(np.random.uniform(0.5, 1))
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight*0.2);")
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight*0.3);")
        time.sleep(np.random.uniform(0.5, 1))
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight*0.45);")
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight*0.6);")
        time.sleep(np.random.uniform(1.5, 2))
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight*0.75);")
        time.sleep(np.random.uniform(0.5, 1))
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight*0.9);")
        time.sleep(np.random.uniform(0.5, 1))
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        time.sleep(3)


        ### only select each country this time and deselect the rest

        deet = []

        try:

            #1: business name, 5: location, 7: sectors, 8: principal authority name, 11: phone number
            for x in [1, 5, 7, 8, 11]:
                path = "(//div[@class='slds-form-element slds-form-element_readonly slds-grow slds-hint-parent override--slds-form-element'])" + str([x])
                element = driver.find_element(By.XPATH, path)
                element = element.text
                element = element.split('\n')[1]
                print(element)
                deet.append(element)

            path = "(//ul[@class='slds-list_dotted'])/li"
            names = driver.find_elements(By.XPATH, path)
            
            list = []
            for name in names:
                list.append(name.text)
            string = ', '.join(list)
            deet.append(string)

        except:
            pass

        deets.extend([deet])

        print('deets', deets)


        
    except Exception as ex:
        print(ex)
        driver.quit()
    finally:
        driver.quit()


# write data into a list to be exported to CSV file


with open('gangmasters.csv', 'w', newline='') as csv_file:
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow(['Business name', 'location', 'Sector', 'Principal authority name', 'phone number', 'Authorised Persons or Postholders Job Title Counts'])
    for line in deets:
        csv_writer.writerow(line)