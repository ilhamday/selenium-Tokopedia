import os
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import requests, time

options = Options()

options.add_argument("--disable-infobars")
options.add_argument("--disable-extensions")

# handle pop up notification in browser
# Pass the argument 1 to allow and 2 to block
options.add_experimental_option("prefs", {
    "profile.default_content_setting_values.notifications": 2
})

driver = webdriver.Chrome(options=options, executable_path=os.path.abspath('chromedriver'))
driver.get('https://www.tokopedia.com/')

def login():
    # jangan lupa delete kalau mau push
    email = 'donizack69@gmail.com'
    password = 'donizack111'

    # email = input('email: ')
    # password = input('password: ')

    btn_login = driver.find_element_by_xpath('//button[@type="button" and @data-testid="btnHeaderLogin"]')
    btn_login.click()

    time.sleep(5)

    # input email to form
    driver.find_element_by_xpath('//input[@id="email-phone"]').send_keys(email)

    # klik next button
    driver.find_element_by_xpath('//button[@id="email-phone-submit"]').click()

    time.sleep(5)
    # input password
    driver.find_element_by_xpath('//input[@id="password-input"]').send_keys(password)

    label = driver.find_element_by_xpath('//label[@class="css-cdg5bv-unf-checkbox e4ba57s2"]')
    checkbox = driver.find_element_by_xpath('//span[@class="css-12a5v84-unf-checkbox__area e4ba57s1"]')

    # driver.find_element_by_xpath('//input[@type="checkbox" and @class="css-dwbw3u-unf-checkbox__input e4ba57s4"]').click()

    ActionChains(driver).move_to_element(label).click(checkbox).perform()
    time.sleep(2)

    driver.quit()

login()

