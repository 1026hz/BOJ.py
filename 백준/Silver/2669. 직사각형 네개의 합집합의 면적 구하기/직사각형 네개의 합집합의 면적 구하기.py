xy = [[0]*100 for _ in range(100)]
cnt = 0

for _ in range(4):
    a,b,c,d = map(int, input().split())
    
    for i in range(a,c):
        for j in range(b,d):
           if xy[i][j] == 0:
              xy[i][j] = 1
              cnt += 1

print(cnt)