A,B = map(int, input().split())
if A>B:
    max = A
    min = B
    print(max-min-1)
    lst = [i for i in range(min+1,max)]
    print(*lst)
elif A<B:
    max = B
    min = A
    print(max-min-1)
    lst = [i for i in range(min+1,max)]
    print(*lst)
else:
    print(0)

