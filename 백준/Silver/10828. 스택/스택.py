import sys
N = int(sys.stdin.readline())
stack = []

for _ in range(N):
    A = str(sys.stdin.readline().rstrip())

    if A[:4] == "push":
        stack.append(int(A[5:]))

    elif A == "pop":
        if stack:
            print(stack.pop())
        else:
            print(-1)

    elif A == "size":
        print(len(stack))

    elif A == "empty":
        print(0 if stack else 1)

    elif A == "top":
        if stack:
            print(stack[-1])
        else:
            print(-1)
