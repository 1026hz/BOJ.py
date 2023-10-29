N = int(input())
lst = list(map(int, input().split()))
X = lst[0]

for i in range(1, N):
    Y = lst[i]
    A = X
    B = Y

    while (B != 0):
        tmp = A
        A = B
        B = tmp % B

    print(X//A, "/", Y//A, sep="")