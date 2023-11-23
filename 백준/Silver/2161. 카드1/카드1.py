import sys
from collections import deque

N = int(sys.stdin.readline())
q = deque([i for i in range(1, N+1)])

while (len(q) > 1):

    print(q.popleft(), end=" ")
    q.rotate(-1)

print(q[0])
