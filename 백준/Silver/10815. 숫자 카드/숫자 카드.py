import sys

n = int(sys.stdin.readline())
number_card = sorted(list(map(int, sys.stdin.readline().split())))
m = int(sys.stdin.readline())
check = list(map(int, sys.stdin.readline().split()))

for i in check:
    start = 0
    end = n-1
    flag = False

    while start <= end:
        middle = (start+end)//2

        if i == number_card[middle]:
            print(1, end=" ")
            flag = True
            break
        elif i > number_card[middle]:
            start = middle + 1
        else:
            end = middle - 1

    if flag == False and start > end:
        print(0, end=" ")