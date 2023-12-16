import sys
from collections import deque

N = int(sys.stdin.readline())
height = deque()

for _ in range(N):
    height.append(int(sys.stdin.readline()))

criteria = height.pop()
ans = 1

while height:
    stick = height.pop()
    if stick > criteria:
        ans += 1
        criteria = stick

print(ans)
