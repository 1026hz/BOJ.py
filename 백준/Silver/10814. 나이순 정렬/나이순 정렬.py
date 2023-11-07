import sys

N = int(sys.stdin.readline())
agelst = []
lst = []

for _ in range(N):
    age, name = map(str, input().split())
    agelst.append(int(age))
    lst.append([age, name])


agelst = sorted(set(agelst))

for i in agelst:
    for j in range(N):
        if i == int(lst[j][0]):
            print(*lst[j])
