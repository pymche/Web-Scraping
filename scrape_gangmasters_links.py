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


driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://glass.gla.gov.uk/public/s/advanced-search")

linky = []

time.sleep(2)

driver.maximize_window()


time.sleep(5)

action = ActionChains(driver)

#WindowsOS
for x in range(0, 6):
    action.key_down(Keys.CONTROL).send_keys('+').key_up(Keys.CONTROL).perform()

#MacOS
# action.key_down(Keys.COMMAND).send_keys('+').key_up(Keys.COMMAND).perform()


# Navigate to site

# Looping through each industry


# Loop through each industry, scrape data from each page

try:

    # element = WebDriverWait(driver, 10).until(
    #     EC.presence_of_element_located((By.CLASS_NAME, "slds-p-around_small slds-col_bump-left"))
    # )

    time.sleep(5)

    print('A')

    # select located in

    button = driver.find_element(By.XPATH, "//label[@class='slds-radio__label'][1]//span[@class='slds-radio_faux']")
    button.click()

    print('B')

    time.sleep(3)
    
    # <button class="slds-button slds-button_neutral" type="button" data-aura-rendered-by="25:638;a"><!--render facet: 26:638;a-->Next<!--render facet: 29:638;a--></button>
    # <button class="slds-button slds-button_neutral" type="button" data-aura-rendered-by="25:638;a" disabled="true"><!--render facet: 26:638;a-->Next<!--render facet: 29:638;a--></button>


    ### only select each country this time and deselect the rest

    countries = {'England': [2,3,4,5]}
    # 'Scotland': [1,2], 
    # 'Wales': [2, 3], 
    # 'Northern Ireland': [3, 4], 
    # 'Other': [4, 5]}

    for name, country in countries.items():

        for value in country:

            path = "(//div[@class='slds-form-element__control']//span[@class='slds-checkbox_faux'])" + str([value])
            element = driver.find_element(By.XPATH, path)
            element.click()
            time.sleep(2)

            print('selected ', name)

        # search

        button = driver.find_element(By.CLASS_NAME, "slds-button-group")
        button.click()

        print('search again')


        time.sleep(10)

        #drop down list pick 100

        value = 1
        path = "(//select[@name='selectItem'])" + str([value])
        dropdown = Select(driver.find_element(By.XPATH, path))
        time.sleep(2)
        dropdown.select_by_value("100")
        time.sleep(3)

        print('dropdown list selected 100')

        # scroll

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

        # loops through pages

        x = 1

        while x != None:

            # get links
            links = driver.find_elements(By.XPATH, "//tr[@class='slds-hint-parent']//a")
            for link in links:
                link = link.get_attribute("href")
                print(link)
                linky.extend([[link, name, x]])

            time.sleep(5)

            # select next page

            try: 
                print('trying to find next page')
                next = driver.find_element(By.XPATH, "(//div[@class='slds-button-group slds-show arcsharedPaginator']/button[@type='button'])[position()=(last()-1)]")
                print(next.text)
                if next.get_attribute("disabled"):
                    print(next.get_attribute("disabled"))
                    x = None
                else:
                    x = x + 1
                    next.click()

                    time.sleep(55)

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

            except:
                print('last page')

    print('all ', len(linky))


        
except Exception as ex:
    print(ex)
    driver.quit()
finally:
    driver.quit()


# write data into a list to be exported to CSV file


with open('gangmasters_list.csv', 'w', newline='') as csv_file:
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow(['Links', 'Country', 'Page'])
    for line in linky:
        csv_writer.writerow(line)