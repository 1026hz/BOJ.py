N = int(input())
xlst = []
ylst = []
for _ in range(N):
    x,y = map(int, input().split())
    xlst.append(x)
    ylst.append(y)

print((max(xlst)-min(xlst)) * (max(ylst)-min(ylst)))