import sys

s = sys.stdin.readline().rstrip()
ans = ""
ansList = []
flag = False

for i in range(len(s)):

    if s[i] == " " and flag == False:
        ansList.append(ans)
        ansList.append(" ")
        ans = ""
        continue

    if s[i] == "<":
        flag = True
        ans += s[i]

    elif s[i] == ">":
        flag = False
        ans += s[i]
        ansList.append(ans)
        ans = ""

    else:
        if flag == True:
            ans += s[i]

            if i == len(s)-1:
                ansList.append(ans)

        if flag == False:
            ans = (s[i] + ans)

            if i == len(s)-1:
                ansList.append(ans)


print(*ansList, sep="")
