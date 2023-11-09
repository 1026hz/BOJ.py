import sys
from collections import deque

T = int(sys.stdin.readline())
dic = {}

for _ in range(T):

    N, M = map(int, sys.stdin.readline().split())
    doc = deque([i for i in range(0, N)])
    importance = deque(list(map(int, sys.stdin.readline().split())))

    ans = 0
    while True:
        if max(importance) == importance[0]:
            ans += 1
            importance.popleft()
            num = doc.popleft()

            if (num) == M:
                print(ans)
                break

        else:
            importance.rotate(-1)
            doc.rotate(-1)
