import sys

N, K = map(int, sys.stdin.readline().split())
A = list(map(int, sys.stdin.readline().split()))
sorted = False
cnt = 0

while not sorted:
    sorted = True

    for i in range(N-1):
        if A[i] > A[i+1]:
            A[i], A[i+1] = A[i+1], A[i]
            sorted = False
            cnt += 1

        if cnt == K:
            print(*A)
            break

    if cnt == K:
        break

    N -= 1

if cnt < K:
    print(-1)
