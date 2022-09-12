from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

browser = webdriver.Chrome()
browser.maximize_window() # 창 최대화

url = "https://flight.naver.com/"
browser.get(url)

# 가는 날 선택 클릭
browser.find_element_by_xpath("//*[@id='__next']/div/div[1]/div[4]/div/div/div[2]/div[2]/button[1]").click()

try:
    elem = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH, "//*[@id='__next']/div/div[1]/div[4]/div/div/div[2]/div[2]/button[1]")))
    print(elem.text)
finally:
    browser.quit()