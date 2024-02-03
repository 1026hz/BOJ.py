import sys

N = int(sys.stdin.readline())
num = list(map(int, sys.stdin.readline().split()))
flag = False
ans = 0
score = 1

for i in num:
    if i == 1:
        flag = True
        ans += score
        score += 1
    else:
        flag = False
        score = 1

print(ans)
