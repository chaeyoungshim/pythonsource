# 다나와 로그인

import requests
from bs4 import BeautifulSoup

# payload
login_info = {
    "redirectUrl": "http://www.danawa.com/?src=adwords&kw=GA0000020&gclid=Cj0KCQjwkruVBhCHARIsACVIiOx-N4XL0e_N292Orxy5MLJhpjpSUIhRHRw65HevL5C23tLkx0fgqJ8aAjFvEALw_wcB",
    "loginMemberType": "general",
    "id": "cyshim12",
    "isSaveId": "true",
    "password": "codud6521!",
}

# 헤더정보
headers = {
    "Referer": "https://auth.danawa.com/login?url=http%3A%2F%2Fwww.danawa.com%2F%3Fsrc%3Dadwords%26kw%3DGA0000020%26gclid%3DCj0KCQjwkruVBhCHARIsACVIiOx-N4XL0e_N292Orxy5MLJhpjpSUIhRHRw65HevL5C23tLkx0fgqJ8aAjFvEALw_wcB",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36",
}

# 세션을 이용
with requests.Session() as s:
    # 로그인
    res = s.post("https://auth.danawa.com/login", login_info, headers=headers)
    # print(res.text)

    # 주문/배송 조회
    res = s.get("https://buyer.danawa.com/order/Order/orderList", headers=headers)

    soup = BeautifulSoup(res.text, "lxml")

    # 아이디 찾기
    user_id = soup.find("p", class_="user")
    print(user_id.get_text())

    if user_id in None:
        # 강제 예외 발생
        raise Exception("Login 실패, 아이디나 비밀번호 확인")

    # 상단메뉴 가져오기
    # copy - selector ( css selector)
    # select() : element 를 리스트로 가져옴
    menu_list = soup.select("div > ul.info_list > li")
    print(menu_list)

    for menu in menu_list:
        # 메뉴명, 수량
        proc, val = menu.find("span").get_text().strip()
