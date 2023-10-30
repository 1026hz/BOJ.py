N = int(input())
first = list(map(int, input().split()))
second = list(map(int, input().split()))

for i in range(N):
    if first[i] < 0:
        first[i] = -(first[i])
        if i+1 < N:
            first[i+1] = -(first[i+1])
        elif i+2 < N:
            first[i+2] = -(first[i+2])

    if second[i] > 0:
        second[i] = -(second[i])
        if i+1 < N:
            second[i+1] = -(second[i+1])
        elif i+2 < N:
            second[i+2] = -(second[i+2])

print(sum(first)-sum(second))
