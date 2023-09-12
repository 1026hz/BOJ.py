N,B = map(int, input().split())
word = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
ans = []
i = 0

while True:
    if N == 0:
        break
    if 0 <= N%B < 10:
        ans.append( (N%B) )
    else:
        ans.append( chr(N%B+55) )
    N //= B
    i += 1

for i in range(len(ans)-1,-1,-1):
    print(ans[i], end="")