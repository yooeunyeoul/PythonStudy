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


def 체크함수4_1(n, position):
    if position > 5:
        return -1


if __name__ == '__main__':
    이것이_취업을위한_코테다_예제_4_1_상하좌우()