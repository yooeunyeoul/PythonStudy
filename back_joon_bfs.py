from collections import deque

# n, m = map(int, input().split())
# 3,3

z, p = map(int, input().split())

graph = [[0, 1, 0],
         [1, 1, 1],
         [1, 1, 0]]

visited = [[False, False, False],
           [False, False, False],
           [False, False, False]]


# 1 1 0
# 0 1 0
# 1 1 1
print("")


#     상 하 좌 우

#     큐에다가 1인 숫자 담고
#     조건 = 1이고, -1가 아니고
#     큐에서 빼면서 인접한 애들 큐에 담음
#     큐에서 하나씩 꺼내면서 인접한 애들 숫자 적음
#     마지막 위치에 적힌 숫자를 제출하면 됨

def bfs(n, m):
    queue = deque()
    queue.append((n, m))
    count = 0

    # 위 아래 좌 우

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    while queue:
        x, y = queue.popleft()


        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or ny < 0 or nx >= z or ny >= p:
                continue

            print(nx,ny)
            if visited[nx][ny]:
                continue

            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))
                count += 1
            elif graph[nx][ny] == 0:
                graph[nx][ny] = graph[x][y]
                queue.append((nx, ny))

            visited[nx][ny] = True
            visited[x][y] = True




count = bfs(0, 0)
print(count)
