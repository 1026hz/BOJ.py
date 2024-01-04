import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

if a == b:
    print(1)
    sys.exit(0)

for i in range(n-1, 0, -1):
    largest = i
    for j in range(i):
        if a[j] > a[largest]:
            largest = j

    if i != largest:
        a[i], a[largest] = a[largest], a[i]
        if a == b:
            print(1)
            sys.exit(0)

print(0)
