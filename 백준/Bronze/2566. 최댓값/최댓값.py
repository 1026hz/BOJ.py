A = []

max=0
m = 0
n = 0

for i in range(9):
    A.append(list(map(int,input().split())))

for k in range(9):
    for l in range(9):
        if A[k][l] > max :
            max = A[k][l]
            m = k
            n = l
    
print(A[m][n])
print(m+1, n+1)