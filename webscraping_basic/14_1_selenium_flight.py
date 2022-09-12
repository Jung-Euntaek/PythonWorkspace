import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-logging"])
browser = webdriver.Chrome(options=options)

url = "https://m-flight.naver.com/"
browser.get(url)

begin_data = browser.find_element(By.XPATH, '//button[text() = "가는 날"]')
begin_data.click()

day27 = browser.find_elements(By.XPATH, '//b[text() = "27"]')
day27[0].click()
day31 = browser.find_elements(By.XPATH, '//b[text() = "31"]')
day31[0].click()

# try:
#     elem = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH, "//*[@id='__next']/div/div[1]/div[4]/div/div/div[2]/div[2]/button[1]")))
#     print(elem.text)
# finally:
#     browser.quit()