import sys

n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))
b = list(map(int, sys.stdin.readline().split()))

if a == b:
    print(1)
    sys.exit(0)

for i in range(1, n):
    position = i - 1
    tmp = a[i]

    while (position >= 0 and tmp < a[position]):
        a[position + 1] = a[position]
        position -= 1
        if a == b:
            print(1)
            sys.exit(0)

    if (position + 1 != i):
        a[position + 1] = tmp
        if a == b:
            print(1)
            sys.exit(0)

print(0)
