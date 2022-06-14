# requests + beautifulsoup
# 객체 생성(페이지소스, 파서)
import requests
from bs4 import BeautifulSoup

res = requests.get("https://news.v.daum.net/v/20220613070001362")
# print(res.text)

# parser : html.parser(기본-설치가 필요없음)
# suop = BeautifulSoup(res.text, "html.parser")
soup = BeautifulSoup(res.text, "lxml")
# print(soup)
# print(soup.prettify)

# <head> 태그 안 내용 가져오기
# print(soup.head)

# <body> 태그 안 내용 가져오기
# print(soup.body)

# <title> 태그 안 내용 가져오기
# print(soup.title)
# print(soup.title.name)  # 태그명 가져오기
# print(soup.title.get_text())  # 태그 안 텍스트 가져오기
# print(soup.title.string)  # 태그 안 텍스트 가져오기


# 기사 제목 가져오기
# soup.h3
news_title = soup.find("h3")
print(news_title)
print(news_title.get_text())

# 기사 작성자 가져오기
writer = soup.find("span", "txt_info")
print(writer)
print(writer.get_text())

# 기사 첫 번째 문단 가져오기
para1 = soup.find("p")
print(para1)

print()
contents = soup.find_all("p")
# print(contents)
for para1 in contents:
    print(para1.get_text())
