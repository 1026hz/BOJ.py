import sys
from collections import deque

N, K = map(int, sys.stdin.readline().split())

lst = deque([i for i in range(1, N+1)])
ans = []

while len(lst):
    lst.rotate(-K+1)
    ans.append(lst.popleft())

print("<", end="")
print(*ans, sep=", ", end="")
print(">")
