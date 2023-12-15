import sys

A = list(map(int, sys.stdin.readline().split()))
B = list(map(int, sys.stdin.readline().split()))

A_score = 0
B_score = 0
winner = "D"

for i in range(len(A)):

    if A[i] > B[i]:
        A_score += 3
        winner= "A"
    elif B[i] > A[i]:
        B_score += 3
        winner = "B"
    else:
        A_score += 1
        B_score += 1


print(A_score, B_score)
if A_score == B_score:
    print(winner)
else:
    print("A" if A_score > B_score else "B")
