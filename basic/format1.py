# format()
# ~~.printf("%d",3) 와 같은 개념
# %c - 문자 하나, %f - 실수, %d - 정수, %s - 문자열(만능, 다 됨)

# print('%d' % 100)
# print('%5d' % 100)      # 5자리에 맞춰서 출력
# print('%05d' % 100)     # 5자리 중 비어 있는 자리를 0으로 채워서 출력
# print()
# print("%s" % "hi")
# print("%5s" % "hi")
# print()
# print("%8.2f" % 12.21)  # 기본적으로 오른쪽 정렬
# print("%-8.2f" % 12.21) # - 를 줘서 왼쪽 정렬도 가능
# print("%-8.2f" % 12.2134567)
print()
print("I eat %d apples" % 3)
print("I eat %s apples" % 3)
number = 4
print("I eat %d apples" % number)
print("I eat", number, "apples")
print()
print("%d :  %s" % (1, "홍길동")) # 두 개 이상부터는 괄호로 묶어서 써주기
print("%d  : %s - %f" % (2, "김성호", 93.2))
print("Test1 : %6d Price : %4.2f" % (776,5634.123))
print()
print("I eat %s apples" % 3)
print("I eat %s apples" % 3.156)
print("I eat %s apples" % "3")
print()
print("Error is %d%%" % 98) # 이건 %라는 문자야 라고 알려줘야함 그래서 %% 이렇게 써줘야함 => %가 이미 있기 때문에 %% 써서 % 를 출력할 것이라는 것을 명시