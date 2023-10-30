N = int(input())
tree = []
dist = []

for _ in range(N):
    tree.append(int(input()))

for i in range(0, N-1):
    if abs(tree[i]-tree[i+1]) not in dist:
        dist.append(abs(tree[i]-tree[i+1]))

i = 1
X = dist[i-1]

while (i < len(dist)):
    Y = dist[i]
    while (Y != 0):
        tmp = X % Y
        X = Y
        Y = tmp
    i += 1

print((tree[-1]-tree[0])//X + 1 - len(tree))