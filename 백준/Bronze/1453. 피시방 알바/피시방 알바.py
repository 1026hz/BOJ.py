N = int(input())
lst = list(map(int, input().split()))
no = 0

for i in range(1,N):
    if lst[i] in lst[:i]:
        no += 1

print(no)