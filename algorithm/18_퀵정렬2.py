def quick_sort(list1, start, end):

    # 종료
    if end - start <= 0:
        return

    # 기준값 정하기
    pivot = list1[end]

    i = start

    for j in range(start, end):
        if list1[j] < pivot:
            list1[i], list1[j] = list1[j], list1[i]
            i += 1

    list1[i], list1[end] = list1[end], list1[i]

    # 재귀 호출
    quick_sort(list1, start, i - 1)
    quick_sort(list1, i + 1, end)


if __name__ == "__main__":
    list1 = [6, 8, 3, 9, 10, 1, 2, 4, 7, 5]
    quick_sort(list1, 0, len(list1) - 1)
    print(list1)
