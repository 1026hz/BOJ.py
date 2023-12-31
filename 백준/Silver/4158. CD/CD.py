import sys

N, M = map(int, sys.stdin.readline().split())

while (N != 0 and M != 0):

    sang = []
    sun = []
    cnt = 0

    for _ in range(N):
        sang.append(int(sys.stdin.readline()))

    sang = sorted(sang)

    for _ in range(M):
        sun.append(int(sys.stdin.readline()))

    for i in range(M):
        start = 0
        stop = M-1

        while (start <= stop):
            middle = (start+stop)//2

            if sun[i] == sang[middle]:
                cnt += 1
                break

            elif sun[i] > sang[middle]:
                start = middle+1

            else:
                stop = middle-1

    print(cnt)

    N, M = map(int, sys.stdin.readline().split())
