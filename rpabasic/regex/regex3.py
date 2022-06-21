import re

pattern = re.compile("abcdefgABCDEFG")
print("[] : 괄호 안에 들어가는 문자가 드러 있는 패턴")
print(pattern.search("abc123"))
print(pattern.search("DEG456"))


print()
pattern = re.compile("[a-zA-Z]")
print("[a-zA-Z] : 알파벳 전체를 패턴으로 처리")
print(pattern.search("abc123"))
print(pattern.search("DEG456"))


print()
pattern = re.compile("[a-zA-Z0-9]")
print("[a-zA-Z0-9] : 알파벳 전체를 패턴으로 처리")
print(pattern.search("abc123"))
print(pattern.search("#$%^456"))


print()
pattern = re.compile("[가-힣]")
print("[가-힣] : 한글 찾기")
print(pattern.search("abc123"))  # None
print(pattern.search("가나다라"))  # <re.Match object; span=(0, 1), match='가'>
