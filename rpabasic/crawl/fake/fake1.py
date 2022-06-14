from fake_useragent import UserAgent
from urllib.request import Request, urlopen

url = "https://n.news.naver.com/mnews/article/009/0004975666?sid=100"
try:

    userAgent = UserAgent()
    headers = {"user-agent": userAgent.chrome}

    request_url = Request(url)
    res = urlopen(request_url).read().decode("utf-8")
    print(res)
    print(
        request_url.header_items()
    )  # [('Host', 'n.news.naver.com'), ('User-agent', 'Python-urllib/3.10')]
except Exception as e:
    print(e)
