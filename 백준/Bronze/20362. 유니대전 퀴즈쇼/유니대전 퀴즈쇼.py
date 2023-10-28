N, S = map(str, input().split())
name = []
ans = []
answer = ""
winner = 0
num = 0

for i in range(int(N)):
    a, b = map(str, input().split())

    if a == S:
        answer = b
        winner = i

    name.append(a)
    ans.append(b)

for i in range(int(N)):
    if ans[i] == answer and i < winner:
        num += 1

print(num)
