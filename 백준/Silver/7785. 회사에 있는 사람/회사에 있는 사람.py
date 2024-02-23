import sys

n = int(sys.stdin.readline())
giggle = {}
ans = []

for _ in range(n):
    name, status = map(str, sys.stdin.readline().rstrip().split())
    if status == "enter":
        giggle[name] = 1
    else:
        giggle[name] = 0

for n, s in giggle.items():
    if s == 1:
        ans.append(n)

print(*sorted(ans, reverse=True), sep="\n")
