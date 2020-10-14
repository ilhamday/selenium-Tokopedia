import os
from bs4 import BeautifulSoup
import requests, time
from selenium import webdriver
from selenium.webdriver import ActionChains
import csv
import user_pass
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

def login():
    email = user_pass.email
    password = user_pass.password

    # email = input('email: ')
    # password = input('password: ')

    btn_login = driver.find_element_by_xpath('//button[@type="button" and @data-testid="btnHeaderLogin"]')
    btn_login.click()

    time.sleep(5)

    # find input email and fill it
    driver.find_element_by_xpath('//input[@id="email-phone"]').send_keys(email)

    # click next button
    driver.find_element_by_xpath('//button[@id="email-phone-submit"]').click()

    # find input password and fill it
    wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@id="password-input"]')))
    driver.find_element_by_xpath('//input[@id="password-input"]').send_keys(password)

    # Trying to use Expected_Condition
    # driver.find_element_by_xpath('//input[@type="checkbox" and @class="css-dwbw3u-unf-checkbox__input e4ba57s4"]')
    # if checkbox.is_selected():
    #     checkbox.click()
    # wait.until(EC.element_to_be_clickable((By.XPATH, '//input[@type="checkbox" and @class="css-dwbw3u-unf-checkbox__input e4ba57s4"]'))).click()
    # driver.find_element_by_xpath('//button[@type="submit" and @class="css-ufjp7u-unf-btn e1ggruw00"]').click()

    # Trying to use ActionChains
    # label = driver.find_element_by_xpath('//label[@class="css-cdg5bv-unf-checkbox e4ba57s2"]')
    # checkbox = driver.find_element_by_xpath('//span[@class="css-12a5v84-unf-checkbox__area e4ba57s1"]')
    # ActionChains(driver).move_to_element(label).click(checkbox).perform()

    # The problem is I got the wrong understanding...
    driver.find_element_by_xpath('//span[@class="css-12a5v84-unf-checkbox__area e4ba57s1"]').click()

    # click masuk button
    driver.find_element_by_xpath('//button[@class="css-ufjp7u-unf-btn e1ggruw00"]').click()


    # driver.quit()

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

        # item_title_list.append(item_title)
        with open('result_toped.csv', 'a', newline='') as thefile:
            writer = csv.writer(thefile)
            data = [c, item_title]
            writer.writerow(data) # writerow can only take one argument


def export_csv():
    with open('result_toped.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Index','Product Name'])

search("Lampu disco")
export_csv()
get_data()




# halaman yang ada datanya cuma sampe page 101,
# page 102 udah ada pesan errornya
# jadi walaupun data ada banyak, tapi ngga bisa lebih dari 6000 ( maks di halaman 101)