N, I = map(int, input().split())
lst = []

for _ in range(N):
    lst.append(input())

print(sorted(lst)[I-1])