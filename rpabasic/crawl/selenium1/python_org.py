# python.org 접속
from selenium import webdriver
import time


browser = webdriver.Chrome()
browser.get("https://www.python.org")
browser.maximize_window()


time.sleep(3)
browser.quit()
