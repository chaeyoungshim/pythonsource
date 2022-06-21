import re
from tokenize import group

pattern = re.compile("[a-z]")

matched = pattern.match("Dave")
print("match()", matched)
print()
searched = pattern.search("Dave")
print("match()", searched)

print()

# re.sub(패턴, 바꿀문자열, 원본문자열) : 찾아서 바꾸기
ori_text = "DDA D1A D00A DA"
print(re.sub("D.A", "Dave", ori_text))

print()

# findall() : 정규식과 일치하는 모든 문자열을 찾아 리스트로 변환
print(pattern.findall("Game of Life in Python"))
pattenr = re.compile("[a-zA-Z]+")
print(pattern.findall("Game of Life in Python"))

print()
for m in pattern.finditer("Game of Life in Python"):
    # print(m)
    print(m.group())


# split() : 정규식을 기준으로 문자열 분리 후 리스트로 변화
pattern = re.compile(":")
print(pattern.split("python:java"))
