import sys

N = int(sys.stdin.readline())
lst = []

for _ in range(N):
    a, b = map(str, sys.stdin.readline().split())

    if a in lst:
        lst.append(b)

    elif b in lst:
        lst.append(a)

    if a == "ChongChong" or b == "ChongChong":
        lst.append(a)
        lst.append(b)

print(len(set(lst)))
