from collections import deque
import sys

sys.setrecursionlimit(10 ** 6)


def 이것이_취업을위한_코테다_예제_4_1_상하좌우():
    print("")
    startPosition = [1, 1]
    n = 5
    positionList = ["R", "R", "R", "U", "D", "D"]

    for position in positionList:
        if position == "R":
            if startPosition[1] + 1 > n:
                continue
            startPosition[1] = startPosition[1] + 1

        elif position == "L":
            if startPosition[1] - 1 < 1:
                continue
            startPosition[1] = startPosition[1] - 1

        elif position == "D":
            if startPosition[0] + 1 > n:
                continue
            startPosition[0] = startPosition[0] + 1

        elif position == "U":
            if startPosition[0] - 1 < 1:
                continue
            startPosition[0] = startPosition[0] - 1

    print(startPosition)


def BFS():
    print('')

    n = 3
    m = 3
    count = 0

    list = [[1, 1, 0],
            [0, 1, 0],
            [0, 1, 1]]

    queue = deque()
    queue.append((0, 0))
    while queue:
        x, y = queue.popleft()

        print(x, y)


def 체크함수4_1(n, position):
    if position > 5:
        return -1


# BFS 소스코드 구현
def bfs(x, y):
    # 큐(Queue) 구현을 위해 deque 라이브러리 사용
    queue = deque()
    queue.append((x, y))
    # 큐가 빌 때까지 반복하기
    while queue:
        x, y = queue.popleft()
        # 현재 위치에서 4가지 방향으로의 위치 확인
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 미로 찾기 공간을 벗어난 경우 무시
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            # 벽인 경우 무시
            if graph[nx][ny] == 0:
                continue
            # 해당 노드를 처음 방문하는 경우에만 최단 거리 기록
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))
    # 가장 오른쪽 아래까지의 최단 거리 반환
    return graph[n - 1][m - 1]


graph = []
result = []


def dfs_2210(x, y, count, appendStr):
    if x < 0 or y < 0 or x > 4 or y > 4:
        return

    if count > 4:
        # print(appendStr)
        result.append(appendStr)
        return
    else:
        dfs_2210(x - 1, y, count + 1, appendStr + str(graph[x][y]))
        dfs_2210(x + 1, y, count + 1, appendStr + str(graph[x][y]))
        dfs_2210(x, y - 1, count + 1, appendStr + str(graph[x][y]))
        dfs_2210(x, y + 1, count + 1, appendStr + str(graph[x][y]))
        # print(appendStr +str(graph[x][y]))


#  위 아래 좌 우 5번 돌리면 됨
# 종료 조건으로는 5번 카운트 그리고 끝부분인지 체크 하면 됨
# 재귀함수 빠져나갈 조건 구하고


def back_joon_2210():
    n = 5
    m = 5

    for i in range(n):
        graph.append(list(map(int, input())))

    for i in range(5):
        for j in range(5):
            dfs_2210(i, j, 0, str(graph[i][j]))

    realResult = list(set(result))
    print(realResult)


if __name__ == '__main__':
    back_joon_2210()
    # # N, M을 공백을 기준으로 구분하여 입력 받기
    # n, m = map(int, input().split())
    # # 2차원 리스트의 맵 정보 입력 받기
    # graph = []
    # for i in range(n):
    #     graph.append(list(map(int, input())))
    #
    # # 이동할 네 가지 방향 정의 (상, 하, 좌, 우)
    # dx = [-1, 1, 0, 0]
    # dy = [0, 0, -1, 1]
    #
    # # BFS를 수행한 결과 출력
    # print(bfs(0, 0))

    ## n,m을 공백으로 구분하여 입력받기

    ## n,m = map(int ,input().split())

    # 2차원 배열 초기화
    # n= 5
    # m = 5
    # d = [[0]*m for _ in range(n)]

    # print(d)

    # 3개 입력받기
    # x,y,direction = map(int,input().split())

    # 2차원 배열 입력 받기

    # array = []
    # n = 5
    # for i in range(n):
    #     array.append(list(map(int,input().split())))
    #
    # print(array)
