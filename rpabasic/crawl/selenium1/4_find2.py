from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time


browser = webdriver.Chrome()
browser.maximize_window()

browser.get("http://www.python.org")

# 검색 창 찾기
element = browser.find_element(By.ID, "id-search-field")
# 검색 창 초기화
element.clear()
# 검색어 입력
element.send_keys("python")
# 엔터 입력
element.send_keys(Keys.ENTER)


time.sleep(3)
browser.quit()
