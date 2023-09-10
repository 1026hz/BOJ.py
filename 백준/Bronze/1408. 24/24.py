h1, m1, s1 = map(int, input().split(":"))
h2, m2, s2 = map(int, input().split(":"))

now = h1*3600 + m1*60 + s1
start = h2*3600 + m2*60 + s2


if now > start:
    ans = 24*3600 - (now - start)
else:
    ans = start - now

hour = ans//3600
minute = ans%3600//60
second = ans%3600%60


print(f"{hour:02d}:{minute:02d}:{second:02d}")