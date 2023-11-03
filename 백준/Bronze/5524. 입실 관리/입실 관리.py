N = int(input())
lst = []

for _ in range(N):
    lst.append(input())

for i in range(N):
    print(lst[i].lower())