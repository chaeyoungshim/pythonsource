from distutils import dep_util
import requests
from bs4 import BeautifulSoup

url = "https://www.gmarket.co.kr/?jaehuid=200011415&cosemkid=go16169957297764414&gclid=CjwKCAjwnZaVBhA6EiwAVVyv9Ie1GJTRWn0XzKZxY9ftFFROnIatSPlBPZa5Y4pzTj9XRzyXpDqk2RoC6goQAvD%5FBwE"

res = requests.get(url)
soup = BeautifulSoup(res.text, "lxml")
# print(soup.prettify())

# 1차 카테고리 추출하기
one_depth = soup.find_all("a", class_="link__1depth-item")
# print(one_depth)
# for item in one_depth:
#     print(item.get_text())

# 2차 카테고리 추출
item_2deth = soup.find_all("li", "list-item__2depth")
for item in item_2deth:
    print(item)
