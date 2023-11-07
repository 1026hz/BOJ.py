import sys
N = int(sys.stdin.readline())
lst = []

for _ in range(N):
    lst.append(list(map(int, sys.stdin.readline().split())))

lst = sorted(lst)

for i in range(N):
    print(*lst[i])
