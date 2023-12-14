import sys

num = int(sys.stdin.readline())
player = []
count = {}

for _ in range(num):
    name = sys.stdin.readline()[0]
    player.append(name)

    if name not in count:
        count[name] = 1
    else:
        count[name] += 1

flag = False
ans = ""
for k, v in count.items():
    if v >= 5:
        flag = True
        ans += k

if flag == False:
    print("PREDAJA")
else:
    print(*sorted(ans), sep="")
