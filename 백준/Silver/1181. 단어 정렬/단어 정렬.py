N = int(input())
word = []
length = []
ans = []

for _ in range(N):
    w = input()
    word.append(w)
    length.append(len(w))

length = sorted(set(length))
l = 0
realN = len(set(word))

while len(ans) < realN:
    tmp = []
    short = length[l]

    for i in word:
        if len(i) == short:
            if i not in tmp:
                tmp.append(i)

    tmp = sorted(tmp)
    ans += tmp
    l += 1

print(*ans, sep="\n")