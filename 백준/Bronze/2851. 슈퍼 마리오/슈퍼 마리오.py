import sys
score = []
ans = 0
flag = False

for _ in range(10):
    score.append(int(sys.stdin.readline()))

for i in range(10):
    ans += score[i]
    if ans > 100:
        if ans - 100 <= 100 - (ans - score[i]):
            print(ans)
        elif ans - 100 > 100 - (ans - score[i]):
            print(ans-score[i])

        flag = True
        break

if flag == False:
    print(sum(score))