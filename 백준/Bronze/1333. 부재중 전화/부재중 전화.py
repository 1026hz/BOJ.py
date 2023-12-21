import sys

N, L, D = map(int, sys.stdin.readline().split())
time = 0
loop = L

while (time < (L+5)*N-5):

    time += 1
    loop -= 1

    if loop == -5:
        loop = L

    if time % D == 0:
        if loop <= 0:
            break

if time == (L+5)*N-5:
    i = 1
    while True:
        if D * i >= time:
            print(D*i)
            break
        i += 1
else:
    print(time)
