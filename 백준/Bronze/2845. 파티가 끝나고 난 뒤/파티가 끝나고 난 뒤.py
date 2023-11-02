L, P = map(int, input().split())
lst = list(map(int, input().split()))
ans = []

for i in range(5):
    ans.append(lst[i]-L*P)

print(*ans)
