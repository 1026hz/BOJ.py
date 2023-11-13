import sys
N = int(sys.stdin.readline())
lst = []

for _ in range(N):
    lst.append(int(sys.stdin.readline()))

lst = sorted(lst, reverse=True)

print(*lst, sep="\n")
