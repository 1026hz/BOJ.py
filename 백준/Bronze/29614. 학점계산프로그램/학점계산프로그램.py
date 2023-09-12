S = input()
score = {"A":4.0, "B":3.0, "C":2.0, "D":1.0, "F":0.0}
sum = 0
n = 0

for i in range(len(S)):
    if S[i]=="+":
        sum += 0.5
    else:
        sum += score[S[i]]
        n+=1

print(sum/n)