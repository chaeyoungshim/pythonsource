from time import time
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

browser = webdriver.Chrome()
browser.get("http://www.daum.net")
browser.maximize_window()

# 원하는 요소 찾기
element = browser.find_element(By.NAME, "q")
print(
    element
)  # <selenium.webdriver.remote.webelement.WebElement (session="802c5f5059ebbad02c48f2a3cfb7d38c", element="a8daa6b1-ca0d-4c8e-b6ac-c682a7b408b9")>
# 검색어 넣기
element.send_keys("아이폰")
element.send_keys(Keys.ENTER)

time.sleep(3)
browser.quit()
