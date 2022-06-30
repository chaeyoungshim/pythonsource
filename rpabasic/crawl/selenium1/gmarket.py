# gmarket 을 접속하고 상품명 입력한 후 결과 페이지 이동
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

browser = webdriver.Chrome()
browser.get("https://www.gmarket.co.kr/")
browser.maximize_window()

# 검색창 찾기
# element = browser.find_element(By.NAME, "keyword")
# element.send_keys("마스크")
# element.send_keys(Keys.ENTER)
# time.sleep(1)

# # 결과 페이지에서 원하는 요소 추출
# titles = browser.find_elements(By.TAG_NAME, "h3")

# for title in titles:
#     print(title.text)


# BeautifulSoup 이용하는 방식
res = BeautifulSoup(browser.page_source, "lxml")
titles = res.find_all("h3")

for title in titles:
    print(title.get_text())

time.sleep(3)
browser.quit()
