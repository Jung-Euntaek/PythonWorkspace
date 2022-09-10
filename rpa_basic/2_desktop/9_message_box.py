import pyautogui
# pyautogui.countdown(3) 

# 확인 버튼만 있는 팝업
# pyautogui.alert("자동화 수행에 실패하였습니다.", "경고") # 메세지, 타이틀
# 확인 취소 버튼("Okay" / "Cancel")
# result = pyautogui.confirm("계속 진행하시겠습니까?", "확인")
# 사용자 입력
# pyautogui.prompt("파일명을 무엇으로 하시겠습니까?", "입력")
# 암호 입력
pyautogui.password("암호를 입력하세요")