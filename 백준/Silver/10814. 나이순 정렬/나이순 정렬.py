import sys

N = int(sys.stdin.readline())
lst = []

for _ in range(N):
    age, name = map(str, input().split())
    age = int(age)
    lst.append([age, name])

lst.sort(key=lambda x: x[0])

for a, b in lst:
    print(a, b)
