T = int(input())

for _ in range(T):
    A = input()
    B = []

    for i in A:
        if i == "(":
            B.append(i)

        elif i == ")":
            if len(B) != 0 and B[-1] == "(":
                B.pop()
            else:
                B.append(i)
                break

    if len(B) == 0:
        print("YES")
    else:
        print("NO")
