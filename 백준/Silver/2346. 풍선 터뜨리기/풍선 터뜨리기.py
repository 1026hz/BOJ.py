import sys
from collections import deque

N = int(sys.stdin.readline())
lst = list(map(int, sys.stdin.readline().split()))
q = deque([i for i in range(1, N+1)])
ans = []

for i in range(N):
    a = q.popleft()
    ans.append(a)
    if lst[a-1] > 0:
        q.rotate(-lst[a-1]+1)
    else:
        q.rotate(-lst[a-1])

print(*ans)
