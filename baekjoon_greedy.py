# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import bisect
import itertools
import heapq
from collections import deque


def Answer():
    result = 0

    n = 25
    k = 3

    while n >= k:
        while n % k != 0:
            n -= 1
            result += 1

        n //= k
        result += 1

    while n > 1:
        n -= 1
        result += 1


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    n = int(input())
    data = list(map(int, input().split()))
    eachSum = n * [0]
    data.sort()

#     정렬을 한다
#  1 , 1+2 , 1+2+3 , 1+2+3+3 , 1+2+3+3+4 ,
# f(0) = list[0]
# f(1) = f(0)+list[1]
# f(2) = f(1) + list[2]

#  f0 부터 f 4까지 더한다

    for i in range(0, n):
        if i == 0:
            eachSum[0] = data[0]
        else:
            eachSum[i] = eachSum[i - 1] + data[i]

    print(sum(eachSum))

#  이 모든 값을 더한다.


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
