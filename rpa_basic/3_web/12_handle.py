# 탭 전환할 때

import time
from selenium import webdriver

options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-logging"])
browser = webdriver.Chrome(options=options)
browser.maximize_window()

browser.get("https://www.w3schools.com/tags/att_input_type_radio.asp")
curr_handle = browser.current_window_handle # 현재 핸들 정보
print(curr_handle)

# 핸들 전환
browser.find_element_by_xpath('//*[@id="main"]/div[2]/a').click()

handles = browser.window_handles # 모든 핸들 정보
for handle in handles:
    print(handle)
    browser.switch_to.window(handle) # 각 핸들로 이동
    print(browser.title) # 현재 핸들 타이틀
    print()

# 새로 이동된 브라우저(탭)에서 작업
print("현재 핸들 닫기")
browser.close()

# 이전 핸들로 돌아오기
print("처음 핸들로 돌아오기")
browser.switch_to.window(curr_handle)

print(browser.title)

# 브라우저 컨트롤 확인
time.sleep(5)
browser.get("http://daum.net")

time.sleep(5)
browser.quit()