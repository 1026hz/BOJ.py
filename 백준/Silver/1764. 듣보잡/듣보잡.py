import sys

N, M = map(int, sys.stdin.readline().split())
num = 0
dic = {}

for _ in range(N):
    name = sys.stdin.readline().rstrip()
    dic[name] = 1

for _ in range(M):
    name = sys.stdin.readline().rstrip()
    if name in dic.keys():
        num += 1
        dic[name] = 0
    else:
        dic[name] = 1

print(num)
ansList = []

for k, v in dic.items():
    if v == 0:
        ansList.append(k)

print(*sorted(ansList), sep="\n")
