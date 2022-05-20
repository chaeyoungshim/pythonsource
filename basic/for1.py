# for 
# for 변수 in 범위 :

# print(range(5))
# print(list(range(5)))       # 0부터 시작해서 5 전까지 
# print(list(range(1,5)))     # 1부터 5 전까지 
# print(list(range(0,10,2)))  # 0부터 10 전까지 2씩 증가해서
# print(list(range(50,1,-2)))



# 0~9 출력
for i in range(10) :
    print(i, end= " ")

print()

for i in range(1,11) :
    print(i, end=" ")

print()

# 1~100까지 출력
for i in range(1,101) :
    print(i, end = " ")

print()

# 1~100 홀수 출력
for i in range(1, 101, 2) :
    print(i, end = " ")

print()

# 1~100 합계
sum = 0
for i in range(1,101) :
    sum = sum + i
print("1~100 합계" ,sum)

print()

# 사용자에게 숫자를 입력받은 후 1~사용자 입력값까지 합계 구한 후 출력
# num = int(input("숫자 입력 : ")) + 1 # 무조건 1을 더해줘야 함 이 때
# sum = 0
# for i in range(1,num) :
#     sum = sum + i
# print(sum)


# print("1 ~ {} 까지 합 : {}".format(num, sum(range(1,num))))

print() 

# 문자열 출력
word = "dreams" # 인덱싱을 이용해서 문자를 하나씩 가져옴
for s in word :
    print(s)

# 이중 for 문
for i in range(3) :
    for j in range(3) :
        print(j, end=" ")
    print()
    
print()

# 구구단 2~9단 출력하기
# 2 * 1 = 2 이런 형식으로 옆으로 나열, 3단일 떄 줄 바꾸기
for i in range(2,10) :
    for j in range(1,10) :
        print("%d * %d = %d" % (i,j,i*j)) # print("{} * {} = {}".format(i,j,(i*j)), end="\t")
    print()

# break, continue
i=1
while i <= 10 :
    if i == 5 :
        break
    print(i, end=" ")
    i += 1

print()

# i=1
# while i <= 10 :
#    i += 1
#    if i % 2 == 1:
#        continue
#     print(i, end=" ")

print()

# 실습 : 1~10 출력, i가 5인 경우는 출력하지 않음
# for + continue
# for i range(1,11) :
#     if(i == 5) :
#         continue
#     print(i, end=" ")
