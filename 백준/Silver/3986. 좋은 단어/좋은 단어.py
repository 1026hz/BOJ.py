import sys
from collections import deque

N = int(sys.stdin.readline())
ans = 0

for _ in range(N):
    word = deque(sys.stdin.readline().rstrip())
    q = deque([word.popleft()])

    while word:
        w = word.popleft()
        if len(q) != 0:
            if q[-1] == w:
                q.pop()
            else:
                q.append(w)
        else:
            q.append(w)

    if not len(q):
        ans += 1

print(ans)
