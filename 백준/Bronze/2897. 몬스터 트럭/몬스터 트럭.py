R, C = map(int, input().split())
parking = []
ans = [0]*5

for _ in range(R):
    parking.append(input())

for i in range(R-1):
    for j in range(C-1):

        lst = []
        lst.append(parking[i][j])
        lst.append(parking[i][j+1])
        lst.append(parking[i+1][j])
        lst.append(parking[i+1][j+1])

        if lst.count('#') != 0:
            continue
        elif lst.count('X') == 0:
            ans[0] += 1
        elif lst.count('X') == 1:
            ans[1] += 1
        elif lst.count('X') == 2:
            ans[2] += 1
        elif lst.count('X') == 3:
            ans[3] += 1
        elif lst.count('X') == 4:
            ans[4] += 1

print(*ans, sep="\n")