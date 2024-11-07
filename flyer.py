import re
import json
from datetime import datetime, timedelta
import os
import xlwt

import requests
import time
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC

from driver2 import CustomWebDriver

base_url = "https://member.restaurantdepot.com/ipaper/index"

def flyer_download(driver):
    # driver.implicitly_wait(10)
    
    driver.get(base_url)
    dropdown = driver.find_element(By.ID, "ipaper-store-flyer")
    select = Select(dropdown)
    print(select)

    urls = []

    for option in select.options:
        try:
            option.click()
            time.sleep(0.5)
            city_dropdown = driver.find_element(By.ID, "store-flyers")
            city_select = Select(city_dropdown)
            city_select.options[1].click()

            time.sleep(1)

            iframe = driver.find_element(By.ID, "ipaper-flyer-iframe")
            src = iframe.get_attribute("src")
            print(src)
            urls.append(src)
        except Exception as e:
            print(e)
    
    for url in urls:
        driver.get(url)
        # div = driver.find_element(By.ID, "modDownloadPdfBtn")
        WebDriverWait(driver, 10).until(EC.invisibility_of_element_located((By.ID, "preloaderLogoContainer")))

        # Now click the download button
        download_button = driver.find_element(By.ID, "modDownloadPdfBtn")
        download_button.click()
        time.sleep(1)

if __name__ == "__main__":
    driver = CustomWebDriver(is_eager=True)
    
    flyer_download(driver)

    while(True):
        i = 0

