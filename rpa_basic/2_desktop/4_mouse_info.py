import pyautogui
# pyautogui.mouseInfo() # F1 통해 좌표 복사(앞의 숫자 두 개)
# pyautogui.FAILSAFE = False
pyautogui.PAUSE = 1 # 모든 동작에 1초씩 sleep 적용

for i in range(10):
    pyautogui.move(100, 100)