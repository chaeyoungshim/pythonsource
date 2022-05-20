# 입력 : input()

# msg = input()
# print(msg)

# msg = input("이름 입력 : ")
# print(msg)

# num1 = int(input("Num1 : ")) # str
# num2 = int(input("Num2 : ")) # str
# print(num1+num2)    # str로 인식하여 문자 연결함


# 실습
# 년/월/일 형태로 입력 받은 후 10년 후 날짜 출력
# 내 방식
# date = input("날짜 입력(년/월/일) : ")
# year = date[0:4]
# month = date[5:7]
# day = date[8:]

# year = int(year) + 10

# print(str(year) + "년 " + str(month) + "월 " + str(day) + "일 ")
date1 = input("날짜입력(년/월/일) ")
# pos = date1.find("/")
# year = int(date1[:pos]) + 10
# print("입력한 날짜의 10년 후는 ? %s" % (str(year) + "년 " + date1[5:7] + "월 " + date1[8:] + "일 "))

date1 = date1.split("/") # 이렇게도 할 수 있음
print("입력한 날짜의 10년 후는 ? %s" % (str(int(date1[0])+10) + "년 " + date1[1] + "월 " + date1[2] + "일 "))

