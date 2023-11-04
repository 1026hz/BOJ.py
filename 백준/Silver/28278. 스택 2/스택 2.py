import sys

N = int(input())
stack = []

for _ in range(N):
    num = sys.stdin.readline().rstrip()

    if num[0] == "1":
        stack.append(int(num[2:]))

    elif num == "2":
        if len(stack) != 0:
            print(stack[-1])
            stack.pop()
        else:
            print(-1)

    elif num == "3":
        print(len(stack))

    elif num == "4":
        print(1 if len(stack) == 0 else 0)

    elif num == "5":
        if len(stack) != 0:
            print(stack[-1])
        else:
            print(-1)
