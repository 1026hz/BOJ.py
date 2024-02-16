import sys

N = int(sys.stdin.readline())
people = []
score = [1]*N


for _ in range(N):
    x, y = map(int, sys.stdin.readline().split())
    people.append([x, y])


for i in range(N):
    for j in range(N):

        if i == j:
            continue

        if people[i][0] < people[j][0] and people[i][1] < people[j][1]:
            score[i] += 1

print(*score)
