import sys

cup = [True, False, False]

M = int(sys.stdin.readline())

for _ in range(M):
    X, Y = map(int, sys.stdin.readline().split())
    cup[X-1], cup[Y-1] = cup[Y-1], cup[X-1]

if cup.count(True) == 0:
    print(-1)
else:
    print(cup.index(True)+1)
