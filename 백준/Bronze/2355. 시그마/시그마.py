import sys

A, B = map(int, sys.stdin.readline().split())

if A > B:
    A, B = B, A

cnt = (B+1-A)

print((A+B)*cnt//2)
