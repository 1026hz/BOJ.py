import sys

T = int(sys.stdin.readline())
for i in range(T):
    N = sorted(list(map(int, sys.stdin.readline().split())))
    N = N[1:4]
    if N[-1] - N[0] >= 4:
        print("KIN")
    else:
        print(sum(N))