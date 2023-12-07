import sys

N, M = map(int, sys.stdin.readline().split())
Plist = [None]*N
Mlist = [None]*N

for _ in range(M):
    a, b, c = map(str, sys.stdin.readline().split())

    if b == "P":
        Plist[int(a)-1] = 1 if c == "1" else 0

    elif b == "M":
        Mlist[int(a)-1] = 0 if c == "1" else 1

possible = 0
impossible = 0

for i in range(N):

    if Plist[i] == 0 or Mlist[i] == 0:
        impossible += 1

    elif Plist[i] == 1 and Mlist[i] == 1:
        possible += 1

print(possible, N-impossible)
