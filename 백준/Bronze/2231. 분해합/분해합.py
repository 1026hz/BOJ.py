N = int(input())
lst = []
for i in range(1,N):
    sum = 0
    i = str(i)
    for j in range(len(i)):
        sum += int(i[j])
    sum += int(i)
    if sum == N:
        lst.append(i)

if len(lst) == 0:
    print(0)
else:
    print(min(lst))