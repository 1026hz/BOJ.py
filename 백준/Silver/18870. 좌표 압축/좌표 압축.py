import sys

N = int(sys.stdin.readline())
X = list(map(int, sys.stdin.readline().split()))
sortedX = sorted(set(X))
dic = {sortedX[i]: i for i in range(len(sortedX))}

for i in X:
    print(dic[i], end=" ")