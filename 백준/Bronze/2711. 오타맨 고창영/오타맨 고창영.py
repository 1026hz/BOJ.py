T = int(input())

for _ in range(T):
    num, word = map(str, input().split())
    word = word[:int(num)-1] + word[int(num):]
    print(word)