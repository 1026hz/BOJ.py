word = input()
ans = ""

for i in word:
    n = ord(i)-3
    if n < ord('A'):
        n += 26
    ans += chr(n)

print(ans)