import sys

n = int(sys.stdin.readline())
A = sorted(list(map(int, sys.stdin.readline().split())))
m = int(sys.stdin.readline())
check = list(map(int, sys.stdin.readline().split()))

for i in check:
    flag = False
    start = 0
    end = n-1

    while (start <= end):
        middle = (start+end)//2

        if i == A[middle]:
            print(1)
            flag = True
            break

        elif i > A[middle]:
            start = middle+1

        else:
            end = middle-1

    if flag == False:
        print(0)