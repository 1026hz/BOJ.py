list16 = ["0","1","2","3","4","5","6","7","8","9",
          "A","B","C","D","E","F"]
num = input()
n = 0
ans = 0
while True:
    if len(num) == 0:
        break
    ans += list16.index(num[-1]) * (16**n)
    num = num[:-1]
    n+=1
print(ans)