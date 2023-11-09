import sys
from collections import deque

n = int(sys.stdin.readline())
n = deque([i for i in range(1, n+1)])
A = deque(map(int, sys.stdin.readline().split()))
ans = deque()

while len(A):

    if A[-1] == 1:
        ans.appendleft(n.popleft())
        A.pop()

    elif A[-1] == 2:
        ans.appendleft(n.popleft())
        ans[0], ans[1] = ans[1], ans[0]
        A.pop()

    elif A[-1] == 3:
        ans.append(n.popleft())
        A.pop()

print(*ans)
