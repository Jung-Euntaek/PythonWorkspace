import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-logging"])
browser = webdriver.Chrome(options=options)
browser.maximize_window()
browser.get("https://shopping.naver.com/home/p/index.naver")

# 무선 마우스 입력 및 검색
elem = browser.find_element_by_xpath('//*[@id="autocompleteWrapper"]/input[1]')
elem.send_keys("무선마우스")
elem.send_keys(Keys.ENTER)


# 스크롤
# # 지정 위치로 스크롤 내리기
# browser.execute_script("window.scrollTo(0, 1080)") # x, y 좌표
# browser.execute_script("window.scrollTo(0, 2080)")

# 현재 화면 가장 아래로 스크롤
# browser.execute_script("window.scrollTo(0, document.body.scrollHeight)")

# 동적 페이지 스크롤 내리기
interval = 2 # 2초에 한번 스크롤

# 현재 문서 높이 저장
prev_height = browser.execute_script("return document.body.scrollHeight")

# 반복 수행
while True:
    # 스크롤 화면 가장 아래로
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight)")

    # 페이지 로딩 대기(2초)
    time.sleep(interval)

    # 현재 문서 높이 저장
    curr_height = browser.execute_script("return document.body.scrollHeight")
    if curr_height == prev_height: # 높이 변화 없으면
        break

    prev_height = curr_height

# 맨 위로 올리기
browser.execute_script("window.scrollTo(0, 0)")

time.sleep(5)
browser.quit()