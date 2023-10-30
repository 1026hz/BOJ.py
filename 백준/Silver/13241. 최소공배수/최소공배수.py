A, B = map(int, input().split())
X = A
Y = B

while (Y != 0):
    tmp = X % Y
    X = Y
    Y = tmp

print(int(A*B/X))