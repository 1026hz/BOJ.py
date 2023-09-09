import sys
T = int(sys.stdin.readline())

ans = [[10], [1], [2,4,8,6], [3,9,7,1], [4,6], [5], 
       [6], [7,9,3,1], [8,4,2,6], [9,1]]

for _ in range(T):
    a,b = map(int, sys.stdin.readline().split())
    if a == 10:
        print(10)
    else:
        print(ans[a%10][b%(len(ans[a%10]))-1])