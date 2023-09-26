num = input()
ans = []
i = -1
flag = ""

while True:
    n = 1
    res = 0
        
    for _ in range(3):
        res += int(num[i])*n
        i -= 1
        n *= 2
        if i < -len(num):
            flag = "false"
            break

    ans.append( str(res) )

    if flag == "false":
        break


for j in range(len(ans)-1, -1, -1):
    print(ans[j], end="")