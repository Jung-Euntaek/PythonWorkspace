import time
from selenium import webdriver
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-logging"])
browser = webdriver.Chrome(chrome_options=options)
browser.maximize_window()

browser.get("https://www.w3schools.com/tags/tryit.asp?filename=tryhtml5_input_type_checkbox")

browser.switch_to.frame("iframeResult")

# elem = browser.find_element_by_xpath('//*[@id="vehicle1"]')
elem = browser.find_element(By.XPATH, '//*[@id="vehicle1"]')

time.sleep(5)

if elem.is_selected() == False:
    print("선택하기")
    elem.click()
else:
    print("아무것도 안함")

time.sleep(5)

browser.quit()