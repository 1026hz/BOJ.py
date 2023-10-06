N, L = map(int, input().split())
lst = list(map(int, input().split()))
lst = sorted(lst)

for i in range(N):
    if lst[i] <= L:
        L += 1
    else:
        break

print(L)