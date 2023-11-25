import sys
L, P, V = map(int, sys.stdin.readline().split())
n = 1

while (L != 0 and P != 0 and V != 0):
    ans = 0
    ans += V//P*L

    if V % P >= L:
        ans += L

    else:
        ans += V % P

    print(f"Case {n}: {ans}")
    n += 1
    L, P, V = map(int, sys.stdin.readline().split())