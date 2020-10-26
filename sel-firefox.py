import os
from bs4 import BeautifulSoup
import requests, time
import csv

import pandas as pd
from xlrd import open_workbook

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# for chrome this is called -> options
profile = webdriver.FirefoxProfile()
profile.set_preference('dom.webnotifications.enabled', False)
profile.set_preference('dom.push.enabled', False)

driver = webdriver.Firefox(executable_path=os.path.abspath('geckodriver'), firefox_profile=profile)
driver.get('https://www.tokopedia.com/')

wait = WebDriverWait(driver, 10)

def search(item):
    search_bar = driver.find_element_by_xpath('//input[@aria-label="Bidang pencarian"]')
    search_bar.clear()
    time.sleep(5)
    search_bar.send_keys(item)

    button_search = driver.find_element_by_xpath('//button[@aria-label="Tombol pencarian"]')
    button_search.click()

    url = driver.current_url

def get_data():

    item_title_list = []
    item_title_index = []

    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(5)
    # diferent class area between result from click(something) in the home page and search
    # class area -> css-jza1fo
    # class container -> css-1g20a2m
    big_box = driver.find_element_by_class_name('css-jza1fo')

    little_box = big_box.find_elements_by_class_name('css-1g20a2m')
    c = 0
    for lb in little_box:
        item_title = lb.find_element_by_class_name('css-18c4yhp').text

        c += 1
        print(c)
        print(item_title)

        # adding data to csv file
        # dict_data = {
        #     'Index': c,
        #     'Product Name': item_title
        # }
        #
        # with open('result_toped.csv', 'a', newline='') as thefile:
        #     # writer = csv.riter(thefile)
        #
        #     fieldnames = ['Index', 'Product Name']
        #     writer = csv.DictWriter(thefile, fieldnames=fieldnames)
        #
        #     writer.writerow(dict_data) # writerow can only take one argument

        # for pandas
        item_title_list.append(item_title)
        item_title_index.append(c)

    data = {
        'title': item_title_list,
        'index': item_title_index
    }

    return data

def export_csv_pandas():
    data = get_data()

    df = pd.DataFrame(data=data)

    df.to_csv('data_pandas.csv', index=False)

def read_parameter():
    data = pd.read_excel('parameter.xlsx')
    # df = pd.DataFrame(data, columns=['Barang'])
    df = data['Barang']

    for parameter in df:
        search(parameter)

read_parameter()



# halaman yang ada datanya cuma sampe page 101,
# page 102 udah ada pesan errornya
# jadi walaupun data ada banyak, tapi ngga bisa lebih dari 6000 ( maks di halaman 101)