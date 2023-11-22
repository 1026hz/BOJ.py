import sys
N = sys.stdin.readline().rstrip()
lst = []
ans = 1
sn = 0

for i in range(len(N)):

    if '0' <= N[i] <= '8' and N[i] != '6':

        if N[i] not in lst:
            lst.append(N[i])

        else:
            if lst.count(N[i]) < ans:
                lst.append(N[i])
            else:
                lst.append(N[i])
                ans += 1

    elif N[i] == '6' or '9':
        sn += 1


if sn/2 > ans:
    if sn % 2 == 0:
        ans = sn//2
    else:
        ans = sn//2+1

print(ans)
