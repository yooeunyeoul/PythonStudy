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


def CoinAnswer():
    n = 10
    k = 4200
    inputCoin = 0
    divCount = 0
    moc = 0
    namuge = 0

    # list = [1, 5, 10, 50, 100, 1000, 5000, 10000, 50000]
    inputList = []
    if inputCoin <k:
        heapq.heappush(inputList,inputCoin)



    coin = 1000
    while k != 0:
        moc = k // coin
        namuge = k % coin
        k = namuge
        divCount = moc

# 힙에서 가장큰 수를 뽑아서 나누다가 나머지가 0이 되면 바복문 끝남
# 궁금한점은 heap pop에서 list가 0일때 어떻게 되는지??

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    CoinAnswer()

#  이 모든 값을 더한다.


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
