import sys

X = int(sys.stdin.readline())
i = 1

while (X > 0):
    X -= i
    i += 1

if i % 2 == 0:
    print(f"{-X+1}/{i+X-1}")

else:
    print(f"{i+X-1}/{-X+1}")