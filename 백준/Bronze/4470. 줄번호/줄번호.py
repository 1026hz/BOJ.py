N = int(input())
lst = []

for _ in range(N):
    lst.append(input())

for i in range(N):
    print(f"{i+1}. {lst[i]}")
