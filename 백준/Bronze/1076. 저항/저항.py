lst = []
ans = []
color = ["black", "brown", "red", "orange", "yellow", "green",
         "blue", "violet", "grey", "white"]
for _ in range(3):
    lst.append(input())

ans.append(str(color.index(lst[0])))
ans.append(str(color.index(lst[1])))
if lst[2] != "black":
    ans.append(str("0" * color.index(lst[2])))

print(int("".join(ans)))