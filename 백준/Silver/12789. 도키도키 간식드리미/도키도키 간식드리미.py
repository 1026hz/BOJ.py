import sys
N = int(sys.stdin.readline())
students = list(map(int, sys.stdin.readline().split()))
stack = []
num = 1

while students:
    if students[0] == num:
        students.pop(0)
        num += 1

    else:
        while stack:
            if stack[-1] == num:
                stack.pop()
                num += 1
            else:
                break
        stack.append(students[0])
        students.pop(0)

while stack:
    if stack[-1] == num:
        stack.pop()
        num += 1
    else:
        break

print("Sad" if stack else "Nice")
