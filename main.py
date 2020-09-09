import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import requests, time

option = Options()

option.add_argument("--disable-infobars")
option.add_argument("--disable-extensions")

# mengatasi jika ada notifikasi allow or blockyo
# Pass the argument 1 to allow and 2 to block
option.add_experimental_option("prefs", {
    "profile.default_content_setting_values.notifications": 2
})

driver = webdriver.Chrome(options=option, executable_path=os.path.abspath('chromedriver'))
driver.get('https://www.tokopedia.com/')

# pindah ke halaman action figure | bisa dicari di console $('css selectornya copy disini')
driver.find_element_by_css_selector('.css-15j6m2y > div:nth-child(5) > div:nth-child(1) > div:nth-child(1) > a:nth-child(1)').click()

page = driver.page_source
# urls = driver.current_url

driver.quit()

# urls = 'https://www.tokopedia.com/p/mainan-hobi/figure/action-figure'

# req = requests.get(urls, headers={'User-Agent': 'Mozilla/5.0'})

# print(req.status_code)

soup = BeautifulSoup(page, 'html.parser')

container = soup.find_all('div', attrs={'class': 'css-bk6tzz e1nlzfl3'})

for count, action in enumerate(container, 1):
    name = action.find('span', class_='css-1bjwylw').text
    price = action.find('span', class_='css-o5uqvq').text
    print('-------')
    print(count)
    print(f'nama: {name}')
    print(f'harga: {price}')
    time.sleep(3)
