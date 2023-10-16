s = input()
t = int(input())
lst = []

for i in s:
    lst.append(i)

for _ in range(t):
    a, b = map(int, input().split())

    tmp = lst[a]
    lst[a] = lst[b]
    lst[b] = tmp

print(*lst, sep="")