import sys
input = sys.stdin.readline

n, k = map(int, input().split())
a = list(map(int, input().split()))
cnt = 0

for i in range(n-1, 0, -1):
    largest = i

    for j in range(i):
        if a[j] > a[largest]:
            largest = j

    if i != largest:
        cnt += 1
        a[i], a[largest] = a[largest], a[i]

        if cnt == k:
            print(a[largest], a[i])
            break

if cnt < k:
    print(-1)
