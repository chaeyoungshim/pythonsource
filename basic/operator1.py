# 연산자
# 산술연산자 : +, -, *, /(실수), //(정수), %, **
a,b = 5,3
print(a+b,a-b,a*b,a/b,a//b,a%b, a**b)

print()
s1, s2,s3 = "100","100.123","99999999"
print(s1+s2+s3) # + : 연결 =>  100100.12399999999
print(float(s1)+float(s2)+float(s3))
print(int(s1) + 1)  # TypeError: can only concatenate str (not "int") to str

# 복합 대입 연산자 : +=, -=, *=, /=, //=, %=, **=
a = 10
a += 5
print("a",a)
a == 5
print("a",a)
a *= 5
print("a",a)
a /= 5
print("a",a)
a //= 5
print("a",a)
a %= 5
print("a",a)
a ** 5
print("a",a)

# 실습 : 777,777 원
# 화폐교환 : 5만 원/1만 원/5천 원/ 1천 원
money = 777777

man5 = money//50000
money %= 50000

man1 = money//10000
money %= 10000

chun5 = money/5000
money %= 5000

chun1 = money/1000
money %= 1000

print("50000원 : %d 장" % man5)
print("10000원 : %d 장" % man1)
print("5000원 : %d 장" % chun5)
print("1000원 : %d 장" % chun1)
print("나머지 돈 : %d" % money)

# 관계연산자 : ==, !=, >, <, >=, <=
a,b = 10,0
print(a==b, a!=b, a>b, a<b, a>=b, a<=b)

# 논리연산자 : and, or, not
print(100 > 60 and  60 > 15)
# print(100 > 60 &&  60 > 15)
print(100 > 60 or  60 < 15)
print(not 60 < 15)
print(not False)
print(not True)
# print(!True)

# 비트연산자
print(10 & 7)
print(10 | 7)
print((100>60) & (60 > 15))
