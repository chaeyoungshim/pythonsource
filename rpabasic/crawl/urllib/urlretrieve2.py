import urllib.request as req

# 이미지 , html 파일 다운로드

img_url = "https://search.pstatic.net/common/?src=http%3A%2F%2Fblogfiles.naver.net%2FMjAyMjA1MTFfMjE3%2FMDAxNjUyMjQ3NzU5MTA4.XZOskJtdmOWPxr0tbqPjzH90eA45jQd5cKiCXFHN9gMg.oEsyAqzoalJL71MG4a40JSntWg_cJJH69dXYtQdXa_gg.JPEG.flaress2%2FKakaoTalk_20220511_132402699_13.jpg&type=sc960_832"
file_url = "https://www.naver.com"

# 다운로드 받을 경로
path = "./rpabasic/crawl/download/"

try:
    file1, header1 = req.urlretrieve(img_url, path + "cat.png")
    file2, header2 = req.urlretrieve(file_url, path + "naver.html")
except Exception as e:
    print(e)
else:
    print(header1)
    print()
    print(header2)
