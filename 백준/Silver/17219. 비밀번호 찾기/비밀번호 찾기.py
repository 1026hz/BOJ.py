import sys

N, M = map(int, sys.stdin.readline().split())
url = {}

for _ in range(N):
    a, b = map(str, sys.stdin.readline().split())
    url[a] = b

for _ in range(M):
    find = sys.stdin.readline().rstrip()
    print(url[find])