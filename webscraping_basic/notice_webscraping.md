Ch 1.
- extension, open in browser 설치
: vscode 내의 html 코드 열기 가능

Ch 3.
- pip install requests
: 웹에서 html 문서 정보 가져오기

Ch 5.
- 구글에 "user agent string" → "what is my user agent?"
- user agent 복사

Ch 6.
- pip install beautifulsoup4
- pip instal lxml

Ch 3. (rpa)
- "selenium with python" site 참고
- pip install selenium
- Chrome driver 설치
: "chrome://version" 입력 → 버전 확인
: 'chromedriver' 입력, 버전 맞춰 다운로드
: zip 폴더 workspace에 복사 후 압축 풀기 (exe 폴더)

- browser.back(), browser.forward(), browser.refresh(), browser.save_screenshot(), browser.maximize_window()
- browser.close() : 탭 닫기, browser.quit() : 창 닫기
- from selenium.webdriver.common.keys import Keys()
: elem.send_keys(Keys.ENTER) # 엔터 키 입력
- elem.clear() : 텍스트 삭제

Ch 4.
- browser.switch_to.frame("iframe ID") # frame 전환
- browser.switch_to.default_content() # 원래 frame 복귀