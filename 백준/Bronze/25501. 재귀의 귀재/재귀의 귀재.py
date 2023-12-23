import sys


def recursion(s, l, r):
    global num
    num += 1
    if l >= r:
        return 1
    elif s[l] != s[r]:
        return 0
    else:
        return recursion(s, l+1, r-1)


def isPalindrome(s):
    return recursion(s, 0, len(s)-1)


T = int(sys.stdin.readline())

for _ in range(T):
    num = 0
    S = sys.stdin.readline().rstrip()
    print(isPalindrome(S), num)
