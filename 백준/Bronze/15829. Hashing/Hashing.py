import sys
L = int(sys.stdin.readline().rstrip())
word = sys.stdin.readline().rstrip()
ans = 0
for i in range(L):
    ans +=((ord(word[i])-96)*(31**i))
print(ans)