# 선택 정렬 : 정렬 알고리즘 중 쉬운 방법

# 이중 for 문 사용 - 특정 위치부터 자료 값 중 최솟값의 위치를 찾은 후
# 정렬을 원하는 자리와 교환
def selection_sort1(list1):
    size = len(list1)

    for i in range(0, size - 1):
        min_idx = i  # 처음 돌 때는 0번
        for j in range(i + 1, size):  # 1번 요소부터 시작할 것, 최소값의 위치 찾기
            if list1[j] < list1[min_idx]:
                min_idx = j  # j로 바꾸기

        # 찾은 최소값과 정렬위치 교환(서로 바꿔주기)
        list1[i], list1[min_idx] = list1[min_idx], list1[i]


# 내림차순
def selection_sort2(list1):
    size = len(list1)

    for i in range(0, size - 1):
        max_idx = i  # 처음 돌 때는 0번
        for j in range(i + 1, size):  # 1번 요소부터 시작할 것, 최소값의 위치 찾기
            if list1[j] > list1[max_idx]:
                max_idx = j  # j로 바꾸기

        # 찾은 최소값과 정렬위치 교환(서로 바꿔주기)
        list1[i], list1[max_idx] = list1[max_idx], list1[i]


if __name__ == "__main__":
    list1 = [35, 9, 2, 85, 17]

    # print("오름차순")
    # selection_sort1(list1)
    # print(list1)

    print("내림차순")
    selection_sort2(list1)
    print(list1)
