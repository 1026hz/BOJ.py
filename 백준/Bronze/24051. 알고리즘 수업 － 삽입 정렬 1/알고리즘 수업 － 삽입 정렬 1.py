import sys

n, k = map(int, sys.stdin.readline().split())
a = list(map(int, sys.stdin.readline().split()))
cnt = 0

for i in range(1, n):
    position = i - 1
    tmp = a[i]

    while (position >= 0 and tmp < a[position]):
        cnt += 1
        a[position + 1] = a[position]

        if cnt == k:
            print(a[position+1])
            sys.exit(0)

        position -= 1

    if (position + 1 != i):
        cnt += 1
        a[position + 1] = tmp

        if cnt == k:
            print(a[position+1])
            sys.exit(0)


print(-1)
