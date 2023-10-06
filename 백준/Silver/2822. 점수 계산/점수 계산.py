score = []
num = []

for _ in range(8):
    score.append(int(input()))

sort_score = sorted(score, reverse=True)

print(sum(sort_score[:5]))

for i in range(5):
    num.append( score.index(sort_score[i])+1 )

print(*sorted(num))