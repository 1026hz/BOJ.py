import sys

N = int(sys.stdin.readline())
lst = []

for _ in range(N):
    a, b = map(int, sys.stdin.readline().split())
    lst.append([b, a])

lst = sorted(lst)

for i in range(N):
    print(lst[i][1], lst[i][0])
