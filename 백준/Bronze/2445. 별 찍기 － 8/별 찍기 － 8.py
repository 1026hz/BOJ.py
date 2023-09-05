N = int(input())
for i in range(1, N+1):
    print("*"*i, " "*(N-i), " "*(N-i), "*"*i, sep="")
for j in range(N-1, 0, -1):
    print("*"*j, " "*(N-j), " "*(N-j), "*"*j, sep="")