import sys

T = int(sys.stdin.readline())

for _ in range(T):
    k = int(sys.stdin.readline()) #층
    n = int(sys.stdin.readline()) #호
    lst = [[0 for i in range(n)]for j in range(k+1)]
    
    for a in range(n):
        lst[0][a] = a+1 #일단 0층 깔아놓기

    for b in range(1,k+1):
        for c in range(n):
            num=0
            for d in range(0,c+1):
                num += lst[b-1][d] 
            lst[b][c] = num

    print(lst[k][n-1])