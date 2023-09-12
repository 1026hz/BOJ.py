N,B = map(str, input().split())
word = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
ans = 0

for i in range(len(N)):
    if N[i] in word[:10]:
        ans += int(N[i]) * (int(B)**(len(N)-i-1))
    else:
        ans += (ord(N[i])-55) * (int(B)**(len(N)-i-1))

print(ans)