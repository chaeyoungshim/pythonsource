# https://news.nate.com/rank/interest?sc=ent 랭킹 뉴스 추출
# 제목, 기사제공자(연합뉴스)

import requests
from bs4 import BeautifulSoup

url = "https://news.nate.com/rank/interest?sc=ent"

res = requests.get(url)
soup = BeautifulSoup(res.text, "lxml")

# 1~5위 가져오기(타이틀, 기사작성자)
# div.mduSubjectList f_clear
top5_list = soup.select("div.mduSubjectList > div")
# print(top5_list)

# 6~50위 가져오기
top45_list = soup.select("#postRankNews li")

for idx, news in enumerate(top5_list, 1):
    # 타이틀
    title = news.select_one("a strong").get_text()  # 이렇게만 하면 a 의 자손인 strong
    # 신문사
    media = news.select_one("span.medium").get_text()
    print(f"{title} - {media}")

for idx, news in enumerate(top45_list, 6):
    # 타이틀
    title = news.select_one("a strong").get_text()  # 이렇게만 하면 a 의 자손인 strong
    # 신문사
    media = news.select_one("span.medium").get_text()
    print(f"{idx} : {title} - {media}")
