N, M = map(int, input().split())
lst = list(map(int, input().split()))
ans = []

for i in range(1, N+1):
    for j in range(0, M):
        if i % lst[j] == 0:
            ans.append(i)

ans = set(ans)
print(sum(ans))