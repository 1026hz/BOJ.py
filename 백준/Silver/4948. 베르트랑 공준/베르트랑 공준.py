import math
num = int(input())

while (num != 0):
    lst = [0 for _ in range(2*num+1)]
    lst[0] = 1
    lst[1] = 1

    for i in range(2, int(math.sqrt(2*num))+1):
        if lst[i] == 0:
            for j in range(i+i, 2*num+1, i):
                lst[j] = 1

    lst = lst[num+1: 2*num+1]
    print(lst.count(0))

    num = int(input())