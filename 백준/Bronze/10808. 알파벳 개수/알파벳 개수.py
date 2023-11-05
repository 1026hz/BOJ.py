S = input()
lst = [0]*26

for i in range(len(S)):
    lst[ord(S[i])-97] += 1

print(*lst)