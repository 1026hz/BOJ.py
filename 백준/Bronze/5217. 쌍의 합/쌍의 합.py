T= int(input())
for _ in range(T):
    n = int(input())
    lst = []
    for i in range(1,n//2+1):
        if i != n-i :
            lst.append(str(f"{i} {n-i}"))
    print(f"Pairs for {n}: ", end="")
    print(*lst, sep=", ")