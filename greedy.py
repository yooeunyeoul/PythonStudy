import heapq


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


def 그리디문제():
    n = 5
    m = 8
    k = 3

    list = [2, 4, 5, 4, 6]

    list.sort(reverse=True)

    maxValue = list[0]
    secondMaxValue = list[1]
    sumCount = 1
    maxSum = 0
    for i in range(m):
        if sumCount > k:
            sumCount = 1
            maxSum += secondMaxValue
        else:
            sumCount += 1
            maxSum += maxValue

    print(maxSum)


# def 백준2839설탕문제():
#     saltsBox = [3, 5]
#     minCount = 0
#     n = 18
#
#     if (n < saltsBox[0]):
#         print(-1)
#     else:
#         while n != 0:


# n이 주어진다
# 1이 되는 조건
#
# n이 5 혹은 3으로 뺐을 때, 0 or 3의배수 or 5의배수가 아니면 -1

# 최소 카운트
# 6 이 5의 배수인가? 3의배수인가? 둘 다 아니라면? 3이나 5를 뺀다
# 13이 5의 배수인가? 3의 배수인가? 둘 다 아니라면 3이나 5를 뺀다 , 뺀 값이  5의 배수인가? 3의 배수인가? 둘 다 아니라면

# 5혹은 3으로 나눴을 때 ,,,,,,,, 나머지가 0혹은 5의배수 3의배수 인가??18

# 14

# 11
# 3을 뺐을 때 3혹은 5의 배수인가?

# 9
# 5를 뺐을 때 3혹은 5의 배수인가?

# 23  -3 , 20 4   = 5
# 23 -5 18 6 = 7
# 18

# 3을 뺏을때와 5를 뺐을 때의 값의 최소값을 구하면 됨

# 값을 뺏을 때 3의 배수인지 5의 배수인지 체크하는 함수를 재귀로 만들면 됨



# 5로 뺄지 3으로 뺄지
# 빼고 나서 그 값이 3의 배수 5의 배수인지 체크하는게 핵심임
# 그리고 무조건 5의 배수 먼저 체크해야함

def 재귀함수_3을_뺐을때_5를_뺐을때_최소값(minusNumber, n):
    moc = 0

    minusedNumber = n - minusNumber

    moc += 1

    if minusedNumber % 5 == 0:
        moc = minusedNumber / 5 + moc
        return moc

    elif minusedNumber % 3 == 0:
        moc = minusedNumber / 3 + moc
        return moc

    else:
        return 1100


if __name__ == '__main__':
    # print_hi("ㅇㅏㄴ녕" ';')
    saltsBox = [3, 5]
    minCount = 0

    n = 26

    # 21 6 + 15

    # 21 -3 = 18 -3 = 15 -5 10 -5 5 -5 0

    list = []

    for salt in saltsBox:
        num = 재귀함수_3을_뺐을때_5를_뺐을때_최소값(salt, n)
        heapq.heappush(list, int(num))

    print(list)
    if(list[0] == 1100):
        print(-1)
    else:
        print(list[0])

