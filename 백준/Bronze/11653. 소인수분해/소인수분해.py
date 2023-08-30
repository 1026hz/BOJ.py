N = int(input())
first = []
sosu = []

for n in range(1,N):
    if N%n == 0:
        first.append(n)

if len(first)==1:
    print(N)

else:
    for i in range(2,N):
        lst = []
        if N%i==0:
            for j in range(1,i):
                if i%j==0:
                    lst.append(j)
            if len(lst)==1:
                sosu.append(i)
        lst = lst.clear()

    for k in range(len(sosu)):
        while True:
            if N % sosu[k] != 0:
                break
            N = N / sosu[k]
            print(sosu[k])