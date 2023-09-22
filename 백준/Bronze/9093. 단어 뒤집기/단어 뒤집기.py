T = int(input())
for _ in range(T):
    lst = list(map(str, input().split()))
    for i in lst:
        print(i[::-1], end=" ")
    print("")