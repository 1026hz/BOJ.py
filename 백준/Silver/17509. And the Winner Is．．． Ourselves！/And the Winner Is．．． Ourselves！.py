time = []
error = []
cum_time = 0
ans = 0
n = 11

for _ in range(n):
    D, V = map(int, input().split())
    time.append(D)
    error.append(V)

while (n):

    for i in range(n):
        
        if time[i] == min(time):
            cum_time += time[i]
            ans += (cum_time + 20 * error[i])
            error = error[:i] + error[i+1:]
            time = time[:i] + time[i+1:]
            n -= 1
            break

print(ans)
