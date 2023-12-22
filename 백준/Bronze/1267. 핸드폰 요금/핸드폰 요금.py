import sys

N = int(sys.stdin.readline())
calls = map(int, sys.stdin.readline().split())
Y = 0
M = 0

for i in calls:
    Y += (i // 30 + 1)*10
    M += (i // 60 + 1)*15

if M == Y:
    print(f"Y M {M}")
else:
    print(f"M {M}" if M < Y else f"Y {Y}")
