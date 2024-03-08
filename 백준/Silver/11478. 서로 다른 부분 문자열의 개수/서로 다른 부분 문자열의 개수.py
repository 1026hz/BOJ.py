import sys

S = sys.stdin.readline().rstrip()
n = len(S)
cnt = 1
dic = {}
dic[S] = 1

while cnt <= n:

    for i in range(n):
        if S[i:i+cnt] in dic.keys():
            dic[S[i:i+cnt]] += 1
        else:
            dic[S[i:i+cnt]] = 1

    cnt += 1

print(len(dic.keys()))
