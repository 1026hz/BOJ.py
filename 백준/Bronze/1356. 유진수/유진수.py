num = input()
flag = "no"

for i in range(1, len(num)+1):
    if len(num) == 1:
        break
    
    lst1 = num[:i]
    lst2 = num[i:]
    mult1 = 1
    mult2 = 1

    for i in range(len(lst1)):
        mult1 *= int(lst1[i])
    for j in range(len(lst2)):
        mult2 *= int(lst2[j])
    
    if mult1 == mult2 :
        flag = "yes"
        break

if flag == "yes":
    print("YES")
else:
    print("NO")