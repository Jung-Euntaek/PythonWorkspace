from selenium import webdriver
import time

options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-logging"])
browser = webdriver.Chrome(chrome_options=options)

browser.get("https://www.w3schools.com/tags/tryit.asp?filename=tryhtml5_input_type_radio")
browser.maximize_window()

browser.switch_to.frame("iframeResult") # frame 전환(iframe은 별도 접속 필요)

elem = browser.find_element_by_xpath("//*[@id='html']")

# 선택 안 돼있으면 선택하기
if elem.is_selected() == False:
    print("선택 안 돼있으므로 선택하기")
    elem.click()
else:
    print("선택돼 있으므로 아무것도 안함")

time.sleep(5)

if elem.is_selected() == False:
    print("선택 안 돼있으므로 선택하기")
    elem.click()
else:
    print("선택돼 있으므로 아무것도 안함")

browser.quit()
