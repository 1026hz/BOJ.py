import sys
input = sys.stdin.readline

n, k = map(int, input().split())
a = list(map(int, input().split()))
dic = {val: idx for idx, val in enumerate(a)}
b = sorted(a)
cnt = 0

for i in range(n-1, -1, -1):

    if a[i] != b[i]:
        tmp = [a[i], b[i]]
        cnt += 1
        a[i], a[dic[b[i]]] = a[dic[b[i]]], a[i]
        dic[tmp[0]], dic[tmp[1]] = dic[tmp[1]], dic[tmp[0]]

    if cnt == k:
        print(*a)
        sys.exit(0)

print(-1)
