import pyautogui

# fw = pyautogui.getActiveWindow() # 현재 활성화된 창
# print(fw.title) # 창의 제목 정보
# print(fw.size)
# print(fw.left, fw.top, fw.right, fw.bottom)
# pyautogui.click(fw.left + 10, fw.top + 20)

# for w in pyautogui.getAllWindows(): # 모든 윈도우 가져오기
#     print(w)

w = pyautogui.getWindowsWithTitle("스티커 메모")[0]
print(w)
if w.isActive == False:
    w.activate() # 창 활성화

if w.isMaximized == False:
    w.maximize()

w.restore() # 화면 회복

w.close()