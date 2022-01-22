import pyautogui
# 스크린 샷 찍기

# img = pyautogui.screenshot()
# img.save("screenshot.png") # 파일로 저장

#
#pyautogui.mouseInfo()
# 37,19 114,171,236 #72ABEC

pixcel = pyautogui.pixel(37, 19)
print(pixcel)

#print(pyautogui.pixelMatchesColor(37, 19, (114,171,236)))
print(pyautogui.pixelMatchesColor(37, 19, (pixcel)))
