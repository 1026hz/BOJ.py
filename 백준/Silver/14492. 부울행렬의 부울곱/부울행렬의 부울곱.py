N = int(input())
A = []
B = []
C = []

for _ in range(N):
    A.append(list(map(int, input().split())))

for _ in range(N):
    B.append(list(map(int, input().split())))

for i in range(N):
    for j in range(N):
        ans = 0

        for k in range(0, N):
            ans = ans or (A[i][k] and B[k][j])
            
        C.append(ans)

print(C.count(1))