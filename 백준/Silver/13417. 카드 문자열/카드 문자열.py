import sys
from collections import deque

T = int(sys.stdin.readline())

for _ in range(T):
    N = int(sys.stdin.readline())
    lst = deque(map(str, sys.stdin.readline().split()))
    ans = deque()
    ans.append(lst.popleft())

    while len(lst):
        if ord(ans[0]) >= ord(lst[0]):
            ans.appendleft(lst.popleft())

        else:
            ans.append(lst.popleft())

    print(*ans, sep="")
