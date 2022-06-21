# https://news.nate.com/rank/interest?sc=ent 랭킹 뉴스 추출 + 엑셀 저장(nate_오늘날짜.xlsx)
# 시트명 : 연예랭킹뉴스
# 제목, 기사제공자(연합뉴스) 1~50위

import requests
from bs4 import BeautifulSoup
from openpyxl import Workbook
from datetime import datetime  # 오늘 날짜
import re

# 엑셀
wb = Workbook()
ws = wb.active
ws.title = "연예랭킹뉴스"
ws.column_dimensions["A"].width = 70
ws.column_dimensions["B"].width = 15
# 제목 행 추가
ws.append(["기사제목", "신문사"])

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
    # 신문사(신문날사짜) - 한글, 영문문자만 (뉴스엔2022-06-20)
    media_date = news.select_one("span.medium").get_text()

    # re.sub()
    pattern = re.compile("[\d-]+")
    # media = re.sub(pattern, "", media_date)

    # split() => list['마이데일리',2022-06-21]
    media = pattern.split(media_date)
    print(f"{idx} : {title} - {media[0]}")

    # ws.append([title, media])

# for idx, news in enumerate(top45_list, 6):
#     # 타이틀
#     title = news.select_one("a").get_text()  # 이렇게만 하면 a 의 자손인 strong
#     # 신문사
#     media = news.select_one("span.medium").get_text()
#     print(f"{idx} : {title} - {media}")
#     ws.append([title, media])


# 파일명 : clien_220620.xlsx
today = datetime.now().strftime("%y%m%d")
filename = f"nate_{today}.xlsx"
# 엑셀 저장
wb.save("./rpabasic/crawl/download/" + filename)
