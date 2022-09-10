import time
from selenium import webdriver

options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-logging"])
browser = webdriver.Chrome(options=options)
browser.maximize_window()
browser.get("https://www.w3schools.com/tags/tryit.asp?filename=tryhtml_option")

browser.switch_to.frame("iframeResult")

# elem = browser.find_element_by_xpath('//*[@id="cars"]/option[3]')
# elem.click()

time.sleep(3)

# 텍스트 값 통해서 선택(완전 일치)
# elem = browser.find_element_by_xpath('//*[@id="cars"]/option[text()="Audi"]')
# elem.click()

# 텍스트 값 부분일치 항목 선택
elem = browser.find_element_by_xpath('//*[@id="cars"]/option[contains(text(), "Au")]')
elem.click()


time.sleep(5)

browser.quit()