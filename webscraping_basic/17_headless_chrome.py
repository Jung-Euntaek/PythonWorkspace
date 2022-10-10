# 브라우저 직접 안 띄우고 작업

from selenium import webdriver

options = webdriver.ChromeOptions()
options.headless = True
options.add_argument("window-size=1920x1080")

browser = webdriver.Chrome(options=options)
browser.maximize_window()

###################################

browser.get_screenshot_as_file("google_movie.png")