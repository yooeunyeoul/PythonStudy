def dduk(start, end, array, require):
    result = 0
    while start <= end:
        middle = (start + end) // 2

        sum = 0
        for i in array:
            cm = i - middle
            if cm > 0:
                sum += cm

        if sum < require:
            end = middle-1
        else:
            result = middle
            start = middle+1
    print(result)

n, requireCM = list(map(int, input().split()))
print(n, requireCM)
array = list(map(int, input().split()))
array.sort()
# 10 15 17 19
print(array)
dduk(start=0, end=array[n - 1], array=array, require=requireCM)
