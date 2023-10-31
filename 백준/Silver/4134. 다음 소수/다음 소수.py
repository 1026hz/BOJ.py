import math

def isPrime(x):
    if x < 2:
        return False
    else:
        for i in range(2, int(math.sqrt(x))+1):
            if x % i == 0:
                return False
    return True


n = int(input())

for _ in range(n):
    num = int(input())

    while True:
        if isPrime(num) == True:
            print(num)
            break
        else:
            num += 1