import pyautogui

# 마우스 이동
# pyautogui.moveTo(100, 100) # 지정한 위치로 마우스 이동(절대좌표)
# pyautogui.moveTo(100, 200, duration=5) # 5초동안 이동

# 상대좌표(현재 커서 위치로부터)
pyautogui.move(100, 100, duration=1)
print(pyautogui.position()) # 마우스 위치
pyautogui.move(100, 100, duration=1)
print(pyautogui.position())

p = pyautogui.position()
print(p[0], p[1]) # (x, y)
print(p.x, p.y) # (x, y)