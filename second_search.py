def binary_search(array,start, end, target):
    while start <= end:
        mid = (start + end) // 2
        print(mid)
        if array[mid] == target:
            return mid
        # 중간점보다 작으면 왼쪽 탐색
        if array[mid] < target:
            start = mid + 1
        else:
            end = mid - 1
    #         중간점 보다 크면

    return None


n, target = list(map(int, input().split()))
array = list(map(int, input().split()))
result = binary_search(array,0, n - 1, target)
if result == None:
    print("없어")
else:
    print(result)

# 시작점과 끝점 그리고 중간점을 뽑는다

# 중간점과 비교를 한다

# 무한 반복문이 돌아가는 조건은 start <= end
