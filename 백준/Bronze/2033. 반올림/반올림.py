import sys

N = sys.stdin.readline().rstrip()
num = int(N)
i = 10

for _ in range(len(N)-1):

    if int(str(num % i)[0]) >= 5:
        num = (num//i+1)*i
    else:
        num = num//i*i

    i *= 10

print(num)