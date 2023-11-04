while True:
    A = input()
    B = []

    if A == ".":
        break

    if A[-1] != ".":
        print("no")
        continue

    for i in A:
        if i == "(" or i == "[":
            B.append(i)
        elif i == ")":
            if len(B) != 0 and B[-1] == "(":
                B.pop()
            else:
                B.append(i)
                break
        elif i == "]":
            if len(B) != 0 and B[-1] == "[":
                B.pop()
            else:
                B.append(i)
                break

    if len(B) == 0:
        print("yes")
    else:
        print("no")
