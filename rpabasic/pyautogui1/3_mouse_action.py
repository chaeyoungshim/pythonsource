import pyautogui

# 마우스 액션 - click, doubleclick, drag and drop, scroll

# 클릭 - 왼/오 클릭
# click() : 현재 위치에서 왼쪽 클릭
# click() : x,y 좌표에서 왼쪽 클릭

# pyautogui.sleep(3)
# print(pyautogui.position())
# pyautogui.click(x=85, y=21, duration=0.5)

# click(clicks=n) : n=2 인 경우 더블클릭
pyautogui.sleep(1)
# pyautogui.click(clicks=5)

# 2초 간격으로 오른쪽 버튼 2번 클릭
# pyautogui.click(clicks=2, interval=2, button="right")


# pyautogui.doubleClick(x=487, y=142)

# pyautogui.rightClick(500, 300)

# mouseDown() / mouseUp()
# pyautogui.moveTo(200, 200)
# pyautogui.mouseDown()
# pyautogui.moveTo(300, 300)
# pyautogui.mouseUp()

# drag(x,y) / dragTo(x,y)
# Point(x=534, y=572) : 실행한 메모장 제목 위치

# 메모장이 있는 곳으로 이동
# pyautogui.moveTo(x=534, y=572)
# # 상대좌표
# # pyautogui.drag(100, 0, duration=0.5)

# 절대좌표
# pyautogui.dragTo(x=885, y=572)


# scroll(값) : 값이 음수이면 아래로 스크롤, 양수이면 위로 스크롤
pyautogui.scroll(-1000)
pyautogui.scroll(1000)
