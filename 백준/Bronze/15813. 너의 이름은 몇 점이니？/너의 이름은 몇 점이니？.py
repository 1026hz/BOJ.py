n = int(input())
name = input()
score = 0

for i in range(n):
    score += (ord(name[i]) - ord("A")+1)

print(score)