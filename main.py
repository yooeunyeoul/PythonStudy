# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import bisect
import itertools
import heapq
from collections import deque

a = 0


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


def print_for():
    array = []
    for i in range(20):
        if i % 2 == 1:
            array.append(i)

    print(array)


def func():
    global a
    a += 1

    for i in range(10):
        func()


def heapsort(iterable):
    h = []
    result = []

    for value in iterable:
        heapq.heappush(h, value)

    for i in range(len(h)):
        result.append(heapq.heappop(h))

    return result


def count_by_range(a, left_value, right_value):
    right_index = bisect.bisect_right(a, right_value)
    left_index = bisect.bisect_left(a, left_value)
    return right_index - left_index


def make1():
    # n, k = map(int, input().split())

    count = 0
    n = 25
    k = 3

    while n != 1:
        if n % k == 0:
            n = n / k
            count = count + 1


        else:
            n = n - 1
            count = count + 1

    print(count)


def make1Answer():
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

    print(result)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    make1Answer()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
