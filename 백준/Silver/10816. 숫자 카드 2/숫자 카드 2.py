import sys

n = int(sys.stdin.readline())
card = list(map(int, sys.stdin.readline().split()))
card_dict = {y: 0 for y in card}

for c in card:
    card_dict[c] += 1

set_card = sorted(list(set(card)))

m = int(sys.stdin.readline())
check = list(map(int, sys.stdin.readline().split()))
cnt = [0]*m

for i in range(m):
    start = 0
    end = len(set_card)-1

    while (start <= end):
        middle = (start+end)//2

        if check[i] == set_card[middle]:
            cnt[i] += card_dict[check[i]]
            break

        elif check[i] > set_card[middle]:
            start = middle+1

        else:
            end = middle-1

print(*cnt)
