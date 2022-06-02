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
if __name__ == '__main__':
    # print_hi("ㅇㅏㄴ녕" ';')
    그리디문제()


