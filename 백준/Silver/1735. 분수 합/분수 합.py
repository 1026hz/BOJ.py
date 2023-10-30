A, B = map(int, input().split())
C, D = map(int, input().split())
X = B
Y = D

while (Y != 0):
    tmp = X % Y
    X = Y
    Y = tmp

denom = int(B*D/X)

num = int(denom/B)*A + int(denom/D)*C

X = denom
Y = num

while (Y != 0):
    tmp = X % Y
    X = Y
    Y = tmp

print(num//X, denom//X)