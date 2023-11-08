import sys

N = int(sys.stdin.readline())
chat = set()
n = 0

for _ in range(N):
    a = sys.stdin.readline().rstrip()

    if a == "ENTER":
        n += len(chat)
        chat = set()

    else:
        chat.add(a)

print(n + len(chat))
