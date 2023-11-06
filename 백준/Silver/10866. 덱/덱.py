import sys
from collections import deque

N = int(sys.stdin.readline())
q = deque([])

for _ in range(N):
    a = sys.stdin.readline().rstrip()

    if a[:10] == "push_front":
        q.appendleft(int(a[11:]))

    elif a[:9] == "push_back":
        q.append(int(a[10:]))

    elif a == "pop_front":
        print(q.popleft() if q else -1)

    elif a == "pop_back":
        print(q.pop() if q else -1)

    elif a == "size":
        print(len(q))

    elif a == "empty":
        print(0 if q else 1)

    elif a == "front":
        print(q[0] if q else -1)

    elif a == "back":
        print(q[-1] if q else -1)
