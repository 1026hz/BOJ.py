n = int(input())

for _ in range(n):
    a,b = map(int, input().split())

    if a<b:
        max = b
        min = a
    else:
        max = a
        min = b
    
    while (min != 0):

        c = max%min
        max = min
        min = c
    
    GCD = max
    LCM = a*b/GCD

    print(int(LCM))