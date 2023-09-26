S = input()
ans = ""

for i in range(len(S)):
    if 48 <= ord(S[i]) <= 57 :
        ans += S[i]

    elif S[i] == " ":
        ans += " "

    else:
        if 65 <= ord(S[i]) <= 90:
            if  ord(S[i]) + 13 > 90:
                ans += chr( ord(S[i]) - 13 )
            else:
                ans += chr( ord(S[i]) + 13 )
            
        elif 97 <= ord(S[i]) <= 122:
            if  ord(S[i]) + 13 > 122:
                ans += chr( ord(S[i]) - 13 )
            else:
                ans += chr( ord(S[i]) + 13 )

print(ans)
