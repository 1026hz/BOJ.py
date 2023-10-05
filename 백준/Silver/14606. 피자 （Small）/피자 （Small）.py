N = int(input())
A = [N]
ans = 0
i = 1

while True:
    if A.count(1)==N:
        break

    A[0]-=1
    A.append(1)

    ans += A[0]*A[i]

    i+=1

print(ans)