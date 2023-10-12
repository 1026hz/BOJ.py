N = int(input())
lst = []
flag = True

for _ in range(N):
    lst.append(input())

for i in range(N):
    for j in range(N):
        if lst[i][j] != lst[j][i]:
            flag = False
            break
    if flag == False:
        break

if flag == True:
    print("YES")

else:
    print("NO")
