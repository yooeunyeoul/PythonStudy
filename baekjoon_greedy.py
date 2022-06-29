# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import bisect
import itertools
import heapq
from collections import deque


def 백준_1931():
    list = [[1, 4],
            [3, 5],
            [0, 6],
            [5, 7],
            [3, 8],
            [5, 9],
            [6, 10],
            [8, 11],
            [8, 12],
            [2, 13],
            [12, 14]]

    # list = [[3, 10],
    #         [2, 2],
    #         [1, 3],
    #         [2, 2],
    #         [9, 10],
    #         [4, 9],
    #         [2, 2]]
    list.sort()
    list.sort(key=lambda x: (x[1], x[0]))
    first = list[0]

    print(first)
    print(list)

    count = 0
    # newlist.append(first)
    count = count + 1
    # print(newlist)
    selectedItem = first
    for i in range(len(list)):
        if list[i][0] > selectedItem[1]:
            print(list[i])
            count += 1
            selectedItem = list[i]
        elif list[i][0] == selectedItem[0]:
            continue

    print(count)


def 백준_1541():
    print("")


def 백준_2217():
    print("")

##풀이
## 반복문 횟수를 늘려나가면서 최소값과 곱해나가면 그 무게가 최대 출력값이 됨
## 2
## 10
## 15
##출력은 20

## 반복문 돌림
## 입력값 = [10 , 15]
## sort 역순으로 함
## [15, 10]
## i == 0 일때  1x 15  ==> (i+1) x list[i]  == > 15
## i == 1 일때  2x10   ==> (i+1) x list[i]  == > 20
## max 를 써서 최대값을 구하면 됨




def 백준_5585():
    money = 1000
    price = 1
    change = [500, 100, 50, 10, 5, 1]
    result = 0

    changeMoney = money - price  ##620

    while changeMoney != 0:
        for i in change:
            if i < changeMoney:
                moc = int(changeMoney / i)
                changeMoney = changeMoney % i

                result += moc
                break

    print(result)


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
    if inputCoin < k:
        heapq.heappush(inputList, inputCoin)

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
    백준_5585()

#  이 모든 값을 더한다.


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
