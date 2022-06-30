# 전체 스크롤 스크립트
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

browser = webdriver.Chrome()
browser.maximize_window()

browser.get("https://shopping.naver.com/home/p/index.naver")

# 검색창 찾기: 마우스 검색어 넣기
element = browser.find_element(By.CLASS_NAME, "_searchInput_search_input_QXUFf")
element.send_keys("마우스")

# 버튼 클릭
browser.find_element(By.CLASS_NAME, "_searchInput_button_search_1n1aw").click()

# 스크롤 이동 : window.scrollTo(x,y)
# browser.execute_script("window.scrollTo(0,1000)")
# browser.execute_script("window.scrollTo(0,2160)")

# browser.execute_script("window.scrollTo(0,document.body.scrollHeight)")

# 동적 페이지 스크롤링

# 2초에 한번씩 스크롤 이동
interval = 2

# 현재 문서 높이 가져와서 저장
prev_height = browser.execute_script("window.scrollTo(0,document.body.scrollHeight)")

while True:
    # 스크롤 이동
    browser.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    # 페이지 로딩 대기
    time.sleep(interval)

    # 스크롤 진행된 후 현재 문서 높이
    curr_height = browser.execute_script("return document.body.scrollHeight")

    if curr_height == prev_height:
        break
    prev_height = curr_height

time.sleep(3)
browser.quit()
