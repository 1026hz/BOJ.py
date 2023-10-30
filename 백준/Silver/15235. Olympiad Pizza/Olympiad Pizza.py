N = int(input())
full = list(map(int, input().split()))
ans = [0]*N
time = 0

while (full.count(0) != N):

    for i in range(N):

        if full[i] != 0:
            time += 1
            full[i] -= 1

            if full[i] == 0:
                ans[i] = time

print(*ans)
