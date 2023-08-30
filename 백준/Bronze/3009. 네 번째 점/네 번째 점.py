A1, A2 = map(int, input().split())
B1, B2 = map(int, input().split())
C1, C2 = map(int, input().split())

lst1 = [A1,B1,C1]
lst2 = [A2,B2,C2]

for i in range(3):
    if lst1.count(lst1[i])==1:
        ans1 = lst1[i]
    if lst2.count(lst2[i])==1:
        ans2 = lst2[i]

print(ans1, ans2)