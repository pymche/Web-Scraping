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
from selenium.webdriver.support.ui import Select


driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://www.rec.uk.com/jobseekers/member-directory?&q=&sector=All%20sectors&placementType=all&sortBy=A%20-%20Z&auditedOnly=false&page=")


text = []


try:

    url_temp = 'https://www.rec.uk.com/jobseekers/member-directory?&page='

    current_page = 1

    while current_page <= 173:

        url = url_temp + str(current_page)
        driver.get(url)
        print('current page:', current_page)


        print('A')


        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(0.5)

        select = Select(driver.find_element_by_id('listing-pagination'))

        print('B')

        select.select_by_value(str(current_page))

        print('C')

        driver.execute_script("window.scrollTo(0, document.body.scrollHeight*0.5);")
        time.sleep(0.5)

        html = driver.find_elements_by_class_name('card__heading')
        # print(html)

        print('D')

        for info in html:
            info = info.text
            print('info')
            print(type(info))
            text.append(info)

        current_page = current_page + 1

        
except Exception as ex:
    print(ex)
    # driver.quit()
finally:
    driver.quit()



print(text)
for x in text:
    print(x)

with open('rec_companies.csv', 'w') as csv_file:
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow(['REC Companies'])
    for line in text:    
        csv_writer.writerow([line])
