n = input()

while n != '0':

    while True:
        ans = 0

        for i in n:
            ans += int(i)

        if len(str(ans)) == 1:
            print(ans)
            break

        n = str(ans)

    n = input()