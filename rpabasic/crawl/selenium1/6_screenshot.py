from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

browser = webdriver.Chrome()
browser.maximize_window()

browser.get("https://www.daum.net/")

# 검색창 찾기
element = browser.find_element(By.NAME, "q")
# 검색어 넣기 + 엔터
element.send_keys("방탄소년단")
element.send_keys(Keys.ENTER)

time.sleep(1)

# 관련검색어 추출
list_top = browser.find_element(By.CSS_SELECTOR, "#netizen_lists_top > span.wsn")

for item in list_top:
    print(item.text)

# 현재 화면 캡쳐
browser.save_screenshot("./rpabasic/crawl/download/image.png")

time.sleep(3)
browser.quit()
