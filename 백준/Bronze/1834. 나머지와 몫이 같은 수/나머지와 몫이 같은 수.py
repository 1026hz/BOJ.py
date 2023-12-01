import sys

N = int(sys.stdin.readline())
M = 1
ans = []

while (M < N):
    ans.append(N*M+M)
    M += 1

print(sum(ans))