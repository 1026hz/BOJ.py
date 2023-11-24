import sys
n = int(sys.stdin.readline())

lst = [1, 1]
cnt = 0

for i in range(2, n):
    cnt += 1
    lst.append(lst[i-2] + lst[i-1])

print(lst[n-1], cnt)