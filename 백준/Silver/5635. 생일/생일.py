n = int(input())
name = []
birth = []

for i in range(n):
    n, d, m, y = map(str, input().split())
    if len(d) == 1:
        d = "0"+d
    if len(m) == 1:
        m = "0"+m
    name.append(n)
    birth.append(y+m+d)

print(name[birth.index(max(birth))])
print(name[birth.index(min(birth))])
