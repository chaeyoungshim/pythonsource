import urllib.request as req

target_url = [
    "https://search.pstatic.net/common/?src=http%3A%2F%2Fblogfiles.naver.net%2FMjAyMjA1MTFfMjE3%2FMDAxNjUyMjQ3NzU5MTA4.XZOskJtdmOWPxr0tbqPjzH90eA45jQd5cKiCXFHN9gMg.oEsyAqzoalJL71MG4a40JSntWg_cJJH69dXYtQdXa_gg.JPEG.flaress2%2FKakaoTalk_20220511_132402699_13.jpg&type=sc960_832",
    "https://www.naver.com",
]

# 다운로드 받을 경로
path_list = [
    "./rpabasic/crawl/download/cat.png",
    "./rpabasic/crawl/download/naver.html",
]

for i, url in enumerate(target_url):

    try:
        res = req.urlopen(url)

        contemts = res.read()

        print("---------------------")

        print("Header info-{} : {}".format(i, res.info()))
        print("http status-{}".format(res.getcode()))
        print("---------------------")

        with open(path_list[i], "wb") as c:
            c.write(contemts)
    except Exception as e:
        print(e)
    else:
        print("성공")
