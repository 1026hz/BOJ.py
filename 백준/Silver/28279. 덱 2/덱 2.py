import sys
from collections import deque

N = int(sys.stdin.readline())
q = deque([])

for _ in range(N):
    a = sys.stdin.readline().rstrip()

    if a[0] == "1":
        q.appendleft(int(a[2:]))

    elif a[0] == "2":
        q.append(int(a[2:]))

    elif a == "3":
        print(q.popleft() if q else -1)

    elif a == "4":
        print(q.pop() if q else -1)

    elif a == "5":
        print(len(q))

    elif a == "6":
        print(0 if q else 1)

    elif a == "7":
        print(q[0] if q else -1)

    elif a == "8":
        print(q[-1] if q else -1)
