A = list(map(str, input().split()))

while (A != ["#", "0", "0"]):

    if (int(A[1]) > 17) or (int(A[2]) >= 80):
        print(A[0], "Senior")

    else:
        print(A[0], "Junior")

    A = list(map(str, input().split()))