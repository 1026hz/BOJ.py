A = input()
B = input()
AB = ""

for i in range(8):
    AB += A[i]
    AB += B[i]

while (len(AB) > 2):

    tmp = ""

    for j in range(0, len(AB)-1, 1):
        tmp += str(int(AB[j]) + int(AB[j+1]))[-1]

    AB = tmp

print(AB)