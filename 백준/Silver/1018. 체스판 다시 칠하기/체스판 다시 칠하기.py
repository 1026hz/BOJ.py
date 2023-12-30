import sys

N, M = map(int, sys.stdin.readline().split())
given = []
result = []

for _ in range(N):
    given.append(sys.stdin.readline().rstrip())

for i in range(N-7):
    for j in range(M-7):
        draw1 = 0
        draw2 = 0

        for a in range(i, i+8):
            for b in range(j, j+8):
                if (a+b) % 2 == 0:
                    if given[a][b] != "B":
                        draw1 += 1
                    if given[a][b] != "W":
                        draw2 += 1
                else:
                    if given[a][b] != "W":
                        draw1 += 1
                    if given[a][b] != 'B':
                        draw2 += 1

        result.append(draw1)
        result.append(draw2)

print(min(result))
