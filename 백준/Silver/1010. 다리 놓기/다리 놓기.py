import sys

def fact(x):
    ans = 1
    for i in range(1, x+1):
        ans *= i
    return ans

T = int(sys.stdin.readline())

for _ in range(T):
    N, M = map(int, sys.stdin.readline().split())
    print(int(fact(M) / (fact(M-N) * fact(N))))
