import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-logging"])
browser = webdriver.Chrome(options=options)
browser.get("https://www.w3schools.com/html/")
browser.maximize_window()

time.sleep(5)

# 특정 영역 스크롤
elem = browser.find_element_by_xpath('//*[@id="leftmenuinnerinner"]/a[62]')

# 방법 1 : ActionChain
# actions = ActionChains(browser)
# actions.move_to_element(elem).perform()

# 방법 2 :
# xy = elem.location_once_scrolled_into_view # 함수 아니고 변수(() 필요 없음), 좌표 찾는 변수(dict 형태)
# print("value : ", xy)

elem.click()

time.sleep(5)
browser.quit()