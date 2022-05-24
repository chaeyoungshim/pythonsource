# List Comprehension

# 리스트 생성 1 ~ 100
# numbers = []
# for n in range(1, 101):
#     numbers.append(n)

# print(numbers)

# numbers = list(range(1, 101))
# print(numbers)

# numbers2 = [n for n in range(1, 101)]
# print(numbers2)

# list1 = ["갑", "을", "병", "정"]
# # 정 글자를 제외하고 출력
# for x in list1:
#     if x != "정":
#         print(x, end=" ")

# print([x for x in list1 if x != "정"])


# 1 ~ 100 숫자 중에서홀수만 출력
list1 = [n for n in range(1, 101) if n % 2 == 1]  # ==> [ 출력할 값, 반복문, 조건문 ]
print(list1)
print()
# 5 글자 이상의 단어만 출력
list2 = ["nice", "study", "python", "anaconda", "abe"]
print([word for word in list2 if len(word) > 5])
print()
# 소문자만 출력
list3 = ["A", "B", "C", "D", "e", "z"]
# for word in list3:
#     if word.islower():
#         print(word)
print([word for word in list3 if word.islower() == True])
print()
# 아래 리스트를 각 요소에 *2 한 후 출력
list4 = [1, 2, 3, 4]
print([x * 2 for x in list4])


print([x * 2 for x in range(5)])
print([x * x for x in range(5)])
