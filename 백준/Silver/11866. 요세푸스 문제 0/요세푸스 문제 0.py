N, K = map(int, input().split())

A = [i for i in range(1,N+1)]
ans = []
i=K-1

while len(A) > 0:
    #print(i, A, ans)
    ans.append(A[i])
    A.remove(A[i])
    i+=(K-1)
    if i > len(A)-1 :
        while (i-(len(A)))>=0:
            i = i-(len(A))
            if len(A)==0:
                break

print("<", end="")
print(*ans, sep=", ", end="")
print(">")