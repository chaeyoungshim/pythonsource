import re

pattern = re.compile("D?A")

print("? : 최소 0 ~ 최대 1")
print(pattern.search("A"))  # <re.Match object; span=(0, 1), match='A'>
print(pattern.search("DA"))  # <re.Match object; span=(0, 2), match='DA'>
print(pattern.search("AA"))  # <re.Match object; span=(0, 1), match='A'>

print()
pattern = re.compile("D*A")
print("* : 최소 0 ~ 최대 무한대")
print(pattern.search("A"))  # <re.Match object; span=(0, 1), match='A'>
print(pattern.search("DA"))  # <re.Match object; span=(0, 2), match='DA'>
print(pattern.search("DDDDDDDDDDDDDDDDDA"))

print()
pattern = re.compile("D+A")
print("* : 최소 ~ 최댇 무한대")
print(pattern.search("A"))  # None
print(pattern.search("DA"))
print(pattern.search("D00000000000000000000A"))


pattern = re.compile("AD{2}A")
print("{n} : n 만큼 반복")
print(pattern.search("ADA"))
print(pattern.search("ADDA"))  # None
print(pattern.search("D00000000000000000000A"))  # None


print()

pattern = re.compile("AD{2,6}A")
print("{n,m} : 최소 n, 최대 m")
print(pattern.search("ADA"))  # None
print(pattern.search("ADDA"))
print(pattern.search("D00000000000000000000A"))
