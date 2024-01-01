N, M, K = map(int, input().split())
student = N+M-K
cnt = 0

while (student >= 0 and N >= 0 and M >= 0):
    N -= 2
    M -= 1
    student -= 3
    cnt += 1

print(cnt-1)