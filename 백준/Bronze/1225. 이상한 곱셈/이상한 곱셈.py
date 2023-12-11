import sys

A, B = map(str, sys.stdin.readline().split())
ans = 0

for i in range(len(A)):
    for j in range(len(B)):
        ans += int(A[i])*int(B[j])

print(ans)
