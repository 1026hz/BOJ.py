import sys

def hap(num):
    num = str(num)
    tmp = int(num)

    for i in num:
        tmp += int(i)

    return tmp


N = int(sys.stdin.readline())

for i in range(1, N):
    if hap(i) == N:
        print(i)
        sys.exit()

print(0)
