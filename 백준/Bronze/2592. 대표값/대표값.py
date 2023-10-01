lst = []
num = []

for i in range(10):
    lst.append(int(input()))

num = [lst.count(lst[0])]
for i in range(1,10):
    if lst[i] not in lst[:i]:
        num.append(lst.count(lst[i]))
    else:
        num.append(0)

print(int(sum(lst)/10))
print(lst[num.index(max(num))])