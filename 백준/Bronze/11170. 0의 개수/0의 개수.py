T = int(input())

for _ in range(T):
    num = 0
    N,M = map(str, input().split())

    for i in range(int(N),int(M)+1):
        num += str(i).count("0")

    print(num)