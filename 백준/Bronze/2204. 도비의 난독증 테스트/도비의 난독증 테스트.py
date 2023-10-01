while True:
    n = int(input())

    if n == 0:
        break

    lst = []
    lowerlst = []

    for _ in range(n):
        A = input()
        lst.append(A)
        lowerlst.append(A.lower())

    lowerAns = sorted(lowerlst)[0]

    for i in range(n):
        b = lst[i].lower()
        if lowerAns == b:
            print(lst[i])