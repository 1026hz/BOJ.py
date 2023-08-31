n = int(input())

while True:
    if n == -1:
        break

    sum = 0
    lst = []
    for i in range(1, n):
        if n%i == 0:
            lst.append(i)
            sum += i
    if sum == n:
        print(f"{n} = ", end="")
        for j in range(0, len(lst)-1):
            print(f"{lst[j]} + ", end="")
        print(f"{lst[-1]}")
    else:
        print(f"{n} is NOT perfect.")
    
    n = int(input())