N = int(input())
vote = []
ans = 0

for _ in range(N):
    vote.append(int(input()))

while True:
    if max(vote) == vote[0] and vote.count(max(vote)) == 1:
        break

    tmp = vote[1:]
    vote[tmp.index(max(tmp))+1] -= 1
    vote[0] += 1
    ans += 1

print(ans)