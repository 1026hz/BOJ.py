import sys

lst = ['+', '-', '*', '/', '=']
A = int(sys.stdin.readline())
ans = A
operand = 0
operator = ""

while True:
    if A == "=":
        print(int(ans))
        break

    if A not in lst:
        operand = int(A)
        if operator == "+":
            ans += operand

        elif operator == "-":
            ans -= operand

        elif operator == "*":
            ans *= operand

        elif operator == "/":
            ans //= operand
    else:
        operator = A

    A = sys.stdin.readline().rstrip()
