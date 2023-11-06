import sys
from collections import deque

N = int(sys.stdin.readline())
queue = deque([])

for _ in range(N):
    a = sys.stdin.readline().rstrip()

    if a[:4] == "push":
        queue.append(a[5:])

    elif a == "pop":
        print(queue.popleft() if queue else -1)

    elif a == "size":
        print(len(queue))

    elif a == "empty":
        print(0 if queue else 1)

    elif a == "front":
        print(queue[0] if queue else -1)

    elif a == "back":
        print(queue[-1] if queue else -1)
