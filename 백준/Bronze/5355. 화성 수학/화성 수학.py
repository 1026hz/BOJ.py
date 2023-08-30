T = int(input())
for _ in range(T):
    A = list(map(str, input().split()))
    num = float(A[0])
    for i in range(1,len(A)):
        if A[i]=='@':
            num*=3
        elif A[i]=="%":
            num+=5
        elif A[i]=="#":
            num-=7
    print("%.2f" %num)