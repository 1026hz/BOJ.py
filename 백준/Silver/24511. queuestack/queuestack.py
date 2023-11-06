import sys
from collections import deque

N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))
B = list(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline())
C = list(map(int, sys.stdin.readline().split()))
q = deque()

for i in range(N):
    if A[i] == 0:
        q.append(B[i])

if len(q) == 0:
    print(*C)
else:
    for j in range(M):
        print(q.pop(), end=" ")
        q.appendleft(C[j])
