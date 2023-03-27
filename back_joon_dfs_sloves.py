# graph = []


R = 0

G = 0

B = 0

graph = [["R", "R", "R", "B", "B"],
         ["G", "G", "B", "B", "B"],
         ["B", "B", "B", "R", "R"],
         ["B", "B", "R", "R", "R"],
         ["R", "R", "R", "R", "R"]]
isGoing = []


# isGoing = [[False, False, False, False, False],
#            [False, False, False, False, False],
#            [False, False, False, False, False],
#            [False, False, False, False, False],
#            [False, False, False, False, False]]


def back_joon_10026(isDisabled):
    # n = int(input())
    global R, G, B
    R = 0
    G = 0
    B = 0
    global isGoing
    n = 5

    # for i in range(n):
    #     graph.append(list(map(str, input())))

    isGoing = [[False] * n for _ in range(n)]

    if (isDisabled):
        for i in range(n):
            for j in range(n):
                if graph[i][j] == "R":
                    graph[i][j] = "G"

    for i in range(n):
        for j in range(n):
            if isGoing[i][j] == False:
                dfs_10026(i, j, graph[i][j], n)
                if graph[i][j] == "R":
                    R += 1
                elif graph[i][j] == "G":
                    G += 1
                elif graph[i][j] == "B":
                    B += 1


    print(R+G+B)
    # print(f"R:${R}, G:${G}, B:${B}")


def dfs_10026(i, j, character, n):
    if i < 0 or j < 0 or i > n - 1 or j > n - 1:
        return

    if character == graph[i][j] and isGoing[i][j] == False:
        isGoing[i][j] = True
        dfs_10026(i - 1, j, character, n)
        dfs_10026(i + 1, j, character, n)
        dfs_10026(i, j - 1, character, n)
        dfs_10026(i, j + 1, character, n)
    else:
        return


back_joon_10026(False)
back_joon_10026(True)
