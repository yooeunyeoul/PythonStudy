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


# 26
# 26에서 5를 뺀다 -->
# 5의 배수의거나 3의 배수인가??

# 맞다면 -->
#  아니라면 --> 26에서 3을 뺀다 -->
# 5의 배수이거나 3의 배수인가?

#  맞다면 --> 23에서 5를 뺀다 -->
#  아니라면 --> -1 출력

def 재귀함수_3을_뺐을때_5를_뺐을때_최소값(n):
    minusedCount = 0
    minusedNumber = n

    while minusedNumber != 0:
        minusedFive = minusedNumber - 5
        minusedThree = minusedNumber - 3
        if minusedFive % 5 == 0 or minusedFive % 3 == 0:
            minusedNumber = minusedFive
            minusedCount += 1
            continue
        elif minusedThree % 5 == 0 or minusedThree % 3 == 0:
            minusedNumber = minusedThree
            minusedCount += 1
            continue
        else:
            minusedCount = -1
            break

    return minusedCount


def three(sugar, count):
    if sugar % 3 != 0:
        three(sugar + 5, count - 1)
    elif sugar % 3 == 0:
        count += sugar // 3
        print(count)



if __name__ == '__main__':
    # print_hi("ㅇㅏㄴ녕" ';')
    sugar = 2

    bag = 0
    while sugar >= 0:
        if sugar % 5 == 0:  # 5의 배수이면
            bag += (sugar // 5)  # 5로 나눈 몫을 구해야 정수가 됨
            print(bag)
            break
        sugar -= 3
        bag += 1  # 5의 배수가 될 때까지 설탕-3, 봉지+1
    else:
        print(-1)
