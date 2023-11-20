import sys
from collections import deque

n = int(sys.stdin.readline())
q = deque()
ans = deque()

for _ in range(n):
    ans.append(int(sys.stdin.readline()))

pm = []
i = 1

while (i <= n):

    q.append(i)
    pm.append("+")

    if q[-1] == ans[0]:
        while (q[-1] == ans[0]):
            pm.append("-")
            q.pop()
            ans.popleft()

            if not len(q):
                break

    i += 1

if len(q):
    print("NO")
else:
    print(*pm, sep="\n")
