N, K = map(int, input().split())
lst = [i for i in range(2, N + 1)]
flag = False

while True:
    P = lst[0]
    lst.remove(P)

    K -= 1
    if K == 0:
        ans = P
        break

    for num in range(P*P, N+1, P):
        if num in lst:
            lst.remove(num)
            K -= 1
            if K == 0:
                ans = num
                break

    if K == 0:
        break

print(ans)