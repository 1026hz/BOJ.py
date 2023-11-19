import sys
N = int(sys.stdin.readline())
room = []
width = 0
length = 0

for _ in range(N):
    room.append(str(sys.stdin.readline().rstrip()))

for i in range(N):
    sleep = 0
    for j in range(N):

        if room[i][j] == ".":
            sleep += 1
        else:
            sleep = 0

        if sleep == 2:
            width += 1


for i in range(N):
    sleep = 0
    for j in range(N):

        if room[j][i] == ".":
            sleep += 1
        else:
            sleep = 0

        if sleep == 2:
            length += 1

print(width, length)
