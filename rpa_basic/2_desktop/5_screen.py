import pyautogui
# 스크린 샷
# img = pyautogui.screenshot()
# img.save("screenshot.png")

# pyautogui.mouseInfo()
# 37,20 64,171,242 #40ABF2


pixel = pyautogui.pixel(37,20) # 띄어쓰기 X
print(pixel)

print(pyautogui.pixelMatchesColor(28,18,pixel))