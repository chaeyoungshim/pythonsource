import requests
from bs4 import BeautifulSoup
from urllib.request import urlretrieve

res = requests.get(
    "https://ko.wikipedia.org/wiki/%EC%84%9C%EC%9A%B8_%EC%A7%80%ED%95%98%EC%B2%A0"
)

soup = BeautifulSoup(res.text, "lxml")
# print(soup.prettify())

# 사진 저장
#
image1 = soup.select_one(
    "#mw-content-text > div.mw-parser-output > table.infobox > tbody > tr:nth-child(1) > td > a > img"
)
print(image1)
print(image1["src"])

# 이미지 다운로드 - urlretrive
path = "./rpabasic/crawl/download/"

# urlretrieve("이미지 원본 경로", "다운받을 경로")
# urlretrieve("http:" + image["src"], "subway1.jpg")

print()
# 두 번째 사진 저장
image2 = soup.select_one("")

print(image2["src"])

urlretrieve()
