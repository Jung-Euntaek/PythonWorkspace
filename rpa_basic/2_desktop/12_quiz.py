# import pyautogui
# import pyperclip

# pyautogui.hotkey("win", "r")
# pyautogui.write("mspaint")
# pyautogui.press("enter")
# pyautogui.sleep(2)
# mspaint = pyautogui.getWindowsWithTitle("제목 없음 - 그림판")
# mspaint[0].maximize()

# txt_btn = pyautogui.locateOnScreen("txt_btn.png", confidence=0.7)
# while txt_btn is None:
#     txt_btn = pyautogui.locateOnScreen("txt_btn.png", confidence=0.7)

# pyautogui.click(txt_btn)

# pyautogui.click(349, 339, duration=0.5)
# pyperclip.copy("참 잘했어요")
# pyautogui.hotkey("ctrl", "v")

# pyautogui.sleep(5)

# mspaint[0].close()
# not_save_btn = pyautogui.locateOnScreen("not_save_btn.png", confidence=0.7)
# while not_save_btn is None:
#     not_save_btn = pyautogui.locateOnScreen("not_save_btn.png", confidence=0.7)

# pyautogui.click(not_save_btn)


import sys
import pyautogui
import pyperclip

pyautogui.hotkey("win", "r")
pyautogui.write("mspaint")
pyautogui.press("enter")

pyautogui.sleep(2)

window = pyautogui.getWindowsWithTitle("제목 없음 - 그림판")[0]
if window.isMaximized == False:
    window.maximize()

txt_btn = pyautogui.locateOnScreen("txt_btn.png")
if txt_btn:
    pyautogui.click(txt_btn, duration=0.5)
else:
    print("찾기 실패")
    sys.exit()

pyautogui.click(349, 339, duration=0.5)
pyperclip.copy("참 잘했어요")
pyautogui.hotkey("ctrl", "v")

pyautogui.sleep(5)

window.close()
pyautogui.sleep(0.5)
pyautogui.press("n")
