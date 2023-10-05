N, K = map(int, input().split())
lst = list(map(int, input().split(",")))
ans = lst

while True:
    if K==0:
        break
    
    ans = lst[:-1]

    for i in range(0,N-1):
        ans[i] = (lst[i+1]-lst[i])

    lst = ans

    K-=1
    N-=1

print(*ans, sep=",")