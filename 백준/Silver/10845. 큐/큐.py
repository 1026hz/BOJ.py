import sys
from collections import deque

N = int(sys.stdin.readline())
q = deque([])

for _ in range(N):
    a = sys.stdin.readline().rstrip()

    if a[:4] == "push":
        q.append(a[5:])

    elif a == "pop":
        print(q.popleft() if q else -1)

    elif a == "size":
        print(len(q))

    elif a == "empty":
        print(0 if q else 1)

    elif a == "front":
        print(q[0] if q else -1)

    elif a == "back":
        print(q[-1] if q else -1)
