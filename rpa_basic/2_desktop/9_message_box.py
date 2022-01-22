# 메세지 박스  3:47:38~
import pyautogui
# print("곧 시작합니다...")
# pyautogui.countdown(3)
# print("자동화 시작")

#메세제띄우기
# pyautogui.alert( "자동화 수행에 실패하였습니다.","경고")# 확인 버튼만 있는 팝업
# result = pyautogui.confirm("계속 진행하시겠습니까?", "확인")# "확인", " 취소" 버튼 
# print(result)

# result = pyautogui.prompt("파일명을 무엇으로 하시겠습니까?", "입력")# 사용자 입력
# print(result)

result = pyautogui.password("암호를 입력하세요", "암호입력")# 암호입력
print(result)

# pyautogui를 구글에서 검색해서 더 공부하면 됨



