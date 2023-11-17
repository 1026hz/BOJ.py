P = int(input())
lst = ["TTT", "TTH", "THT", "THH", "HTT", "HTH", "HHT", "HHH"]

for _ in range(P):
    coin = input()
    ans = [0]*8

    for i in range(0, 38):
        if coin[i:i+3] in lst:
            ans[lst.index(coin[i:i+3])] += 1

    print(*ans)