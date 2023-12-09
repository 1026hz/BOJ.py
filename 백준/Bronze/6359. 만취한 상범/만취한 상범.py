import sys

T = int(sys.stdin.readline())

for _ in range(T):
    n = int(sys.stdin.readline())
    room = [1]*n

    for i in range(2, n+1):
        for j in range(n):

            if (j+1) % i == 0:

                if room[j] == 1:
                    room[j] = 0
                else:
                    room[j] = 1

    print(room.count(1))
