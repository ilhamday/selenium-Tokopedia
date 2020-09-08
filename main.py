import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

option = Options()

option.add_argument("--disable-infobars")
option.add_argument("--disable-extensions")

# Pass the argument 1 to allow and 2 to block
option.add_experimental_option("prefs", {
    "profile.default_content_setting_values.notifications": 2
})

# menggabungkan dua jawaban dari stackoverflow
driver = webdriver.Chrome(options=option, executable_path=os.path.abspath('chromedriver'))
driver.get('https://www.tokopedia.com/')

# pindah ke halaman action figure | bisa dicari di console $('css selectornya copy disini')
driver.find_element_by_css_selector('.css-15j6m2y > div:nth-child(5) > div:nth-child(1) > div:nth-child(1) > a:nth-child(1)').click()

print(driver.title)
# driver.quit()