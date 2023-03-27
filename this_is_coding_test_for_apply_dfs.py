import sys
from collections import deque


def ddd():
    print("fer")
    n = 4
    m = 5
    count = 0

    list = [[0, 0, 1, 1, 0],
            [0, 0, 0, 1, 1],
            [1, 1, 1, 1, 1],
            [0, 0, 0, 0, 0]]

    for i in range(n):
        for j in range(m):
            if 재귀함수(list, i, j, n, m):
                count += 1

    print(count)


def 재귀함수(list, row, col, n, m):
    if row < 0 or row > n - 1 or col < 0 or col > m - 1:
        return False

        # if list[row][col] ==0:
        list[row][col] = 1
        재귀함수(list, row - 1, col, n, m)
        재귀함수(list, row + 1, col, n, m)
        재귀함수(list, row, col - 1, n, m)
        재귀함수(list, row, col + 1, n, m)
        return True
    # return False


def BFS():
    print('')

    n = 4
    m = 4
    count = 0

    list = [[1, 0, 1, 0],
            [1, 1, 1, 1],
            [0, 1, 1, 1],
            [1, 1, 1, 1]]

    # queue = deque([1])
    # v = queue.popleft()
    # print(v)

    if __name__ == '__main__':
        # print('sgasfasdfasff')
        ddd()

    # 좌 우 상 하 체크하면서 인접한 애를 큐에 넣는다

    # 1-> 1

    # 0번부터 차례대로 체크한다 재귀함수로 들어가야함
    # 0번부터 인접한 행렬
    # / {0,0} -> [ [0,1],[1,0] ]
    # / {0,1} -> [ [0,0],[1,1] ]
    # / {0,4} -> [[]]
    # / {1,0} -> [[0,0],[1,1]]
    # / {1,1} -> [[0,1],[1,0],[1,2]]
