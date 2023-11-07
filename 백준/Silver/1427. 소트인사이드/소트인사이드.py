import sys
N = str(sys.stdin.readline().rstrip())
print(*sorted(N, reverse=True), sep="")