import sys

yeondu = sys.stdin.readline().rstrip()

n = int(sys.stdin.readline())
score_board = {}

for _ in range(n):

    team = sys.stdin.readline().rstrip()
    score = 1
    love = []

    for name in ['L', 'O', 'V', 'E']:
        love.append(yeondu.count(name) + team.count(name))

    for i in range(4):
        for j in range(i+1, 4):
            score *= (love[i] + love[j])

    score_board[team] = score % 100

ans = list(score_board.items())
ans.sort(key=lambda x: x[0])
ans.sort(key=lambda x: x[1], reverse=True)
print(ans[0][0])
