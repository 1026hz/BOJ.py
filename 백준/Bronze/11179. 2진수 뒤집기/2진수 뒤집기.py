N = int(input())
binary = []
ans = 0
n = 1

while (N != 0):
    binary.append(N % 2)
    N //= 2

for i in range(len(binary)-1, -1, -1):
    ans += binary[i] * n
    n *= 2

print(ans)
