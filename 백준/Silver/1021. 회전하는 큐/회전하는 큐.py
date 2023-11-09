import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())
q = deque([i for i in range(1, N+1)])
m = deque(list(map(int, sys.stdin.readline().split())))
ans = 0

while len(m):
    if q[0] == m[0]:
        q.popleft()
        m.popleft()
    else:
        ans += 1
        if q.index(m[0]) <= int(len(q)/2):
            q.rotate(-1)
        else:
            q.rotate(1)

print(ans)
