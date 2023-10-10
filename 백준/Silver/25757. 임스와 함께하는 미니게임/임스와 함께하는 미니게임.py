N, game = map(str, input().split())
lst = []

if game == "Y":
    num = 1
elif game == "F":
    num = 2
elif game == "O":
    num = 3

for _ in range(int(N)):
    lst.append(input())

lst = list(set(lst))

print(len(lst)//num)