import sys
from collections import deque

N, K, M = map(int, sys.stdin.readline().split())
num = 0
lst = deque([i for i in range(1, N+1)])
r = -K+1

while len(lst):

    if num % M == 0 and num > 0:
        if r == -K+1:
            r = K
        else:
            r = -K+1

    lst.rotate(r)
    print(lst.popleft())
    num += 1
