import pyautogui
w = pyautogui.getWindowsWithTitle("스티커 메모")[0]
w.activate()

# pyautogui.write("12345")
# pyautogui.write("NadoCoding", interval=1) # 영문, 숫자만 입력 가능

# 커서 이동
# pyautogui.write(["t", "e", "s", "t", "left", "left", "right", "l", "a", "enter"], interval=0.25)

# 특수 문자
# pyautogui.keyDown("shift")
# pyautogui.press("4")
# pyautogui.keyUp("shift")

# 조합키
# pyautogui.keyDown("ctrl")
# pyautogui.press("a")
# pyautogui.keyUp("ctrl") # ctrl + A

# 간편한 조합키
# pyautogui.hotkey("ctrl", "alt", "shift", "a") # 순서대로 눌렀다 역순으로 뗌
# pyautogui.hotkey("ctrl", "a")

import pyperclip
# pyperclip.copy("나도코딩") # 나도코딩 글자를 클립보드 저장
# pyautogui.hotkey("ctrl", "v")

def my_write(text):
    pyperclip.copy(text)
    pyautogui.hotkey("ctrl", "v")

my_write("나도코딩")

# 자동화 프로그램 종료
# win : ctrl + alt + del