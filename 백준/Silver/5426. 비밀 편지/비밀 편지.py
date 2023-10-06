import math
N = int(input())

for _ in range(N):
    message = input()
    num = int(math.sqrt(len(message)))
    lst = [[0]*num for _ in range(num)]
    a = 0
    for i in range(num):
        for j in range(num):
            lst[i][j] = message[a]
            a+=1

    for k in range(num-1,-1,-1):
        for l in range(num):
            print(lst[l][k], end="")
    
    print("")