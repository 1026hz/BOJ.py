octal = input()
binary = ["000", "001", "010", "011", "100", "101", "110", "111"]
ans = []

for i in range(len(octal)):
    ans.append( binary[int(octal[i])] )

while True:
    if len(ans) == 1 and len(ans[0]) == 1:
        break
    if ans[0][0] == "1":
        break
    else:
        ans[0] = ans[0][1:]

print("".join(ans))