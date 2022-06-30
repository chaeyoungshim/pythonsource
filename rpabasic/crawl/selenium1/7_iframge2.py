from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

browser = webdriver.Chrome()
browser.maximize_window()

browser.get(
    "https://www.w3schools.com/tags/tryit.asp?filename=tryhtml5_input_type_radio"
)
time.sleep(1)

# 그냥은 iframe 안에서 못찾아오니까
# iframe 안의 태그 찾기
# iframe 안으로 들어가서 찾아야 함
browser.switch_to.frame("iframeResult")
time.sleep(1)

element = browser.find_element(
    By.XPATH, '//*[@id="html"]'
).click()  # NoSuchElementException
# print(element.text)
time.sleep(1)

# iframe 밖으로 나오기
browser.switch_to.default_content()
time.sleep(1)

# 왼쪽 h1 출력
left = browser.find_element(
    By.XPATH,
    '//*[@id="textareawrapper"]/div/div[6]/div[1]/div/div/div/div[5]/pre[5]/span/span[4]',
)
print(left.text)

time.sleep(3)
browser.quit()
