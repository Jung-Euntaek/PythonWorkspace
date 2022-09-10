from itertools import count
import time
from selenium import webdriver

options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-logging"])
browser = webdriver.Chrome(chrome_options=options)
browser.maximize_window()
browser.get("https://www.w3schools.com/")


browser.find_element_by_xpath('//*[@id="navbtn_tutorials"]').click()
browser.find_element_by_xpath('//*[@id="nav_tutorials"]/div/div/div[2]/a[1]').click()
browser.find_element_by_xpath('//*[@id="topnav"]/div/div[1]/a[10]').click()
browser.find_element_by_xpath('//*[@id="leftmenuinnerinner"]/a[117]').click()

fst_name = "나도"
lst_name = "코딩"
country = "Canada"
subject = "퀴즈 완료하였습니다"

browser.find_element_by_xpath('//*[@id="fname"]').send_keys(fst_name)
browser.find_element_by_xpath('//*[@id="lname"]').send_keys(lst_name)
browser.find_element_by_xpath('//*[@id="country"]').send_keys(country)
browser.find_element_by_xpath('//*[@id="main"]/div[3]/textarea').send_keys(subject)

time.sleep(5)
browser.find_element_by_xpath('//*[@id="main"]/div[3]/a').click()

time.sleep(5)
browser.quit()
