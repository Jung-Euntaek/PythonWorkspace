import requests
from bs4 import BeautifulSoup
from selenium import webdriver

# headers = {
#     "User-Agent" : "Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36",
#     "Accept-Language" : "ko-KR,ko"
#     }
# res = requests.get(url, headers=headers)
# res.raise_for_status()
# soup = BeautifulSoup(res.text, "lxml")

# with open("movie.html", "w", encoding="utf8") as f:
#     f.write(res.text)
#     f.write(soup.prettify()) # html 문서 예쁘게 출력

browser = webdriver.Chrome()
browser.maximize_window()

# 페이지 이동
url = "https://play.google.com/store/movies?utm_source=apac_med&utm_medium=hasem&utm_content=Aug2118&utm_campaign=Evergreen&pcampaignid=MKT-EDR-apac-kr-1003227-med-hasem-py-Evergreen-Aug2118-Sitelink-BKWS%7cONSEM_kwid_43700009359644016_creativeid_416407016592_device_c&gclid=CjwKCAiA4KaRBhBdEiwAZi1zzmaKDu3nv50JjHj-wYsgcUve-tMpCYyImDg5roxBcpPguoJEl6h_TBoCD10QAvD_BwE&gclsrc=aw.ds"
browser.get(url)

# 스크롤 내리기(지정 위치로)
# browser.execute_script("window.scrollTo(0, 1080)") # window 해상도만큼 해당 위치로 스크롤 내리기

import time
interval = 2

# 화면 가장 아래로 스크롤 내리기
# browser.execute_script("window.scrollTo(0, document.body.scrollHeight)")

# # 현재 문서 높이를 가져와서 저장
prev_height = browser.execute_script("return document.body.scrollHeight")

# 반복 수행
while True:
    # 스크롤을 화면 가장 아래로 내림
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight)")

    # 페이지 로딩 대기
    time.sleep(interval)

    # 현재 문서 높이 저장
    curr_height = browser.execute_script("return document.body.scrollHeight")
    if curr_height == prev_height:
        break

    prev_height = curr_height

