import sys

N, M = map(int, sys.stdin.readline().split())
pocketmon = []
dic = {}

for i in range(N):
    name = sys.stdin.readline().rstrip()
    pocketmon.append(name)
    dic[name] = i+1

for _ in range(M):
    question = sys.stdin.readline().rstrip()

    if '0' <= question[0] <= '9':
        print(pocketmon[int(question)-1])
    else:
        print(dic[question])
