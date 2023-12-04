import sys

N = int(sys.stdin.readline())
ans = "666"
cnt = 0

while cnt != N:

    if "666" in str(ans):
        cnt += 1

    ans = int(ans) + 1

print(ans-1)
