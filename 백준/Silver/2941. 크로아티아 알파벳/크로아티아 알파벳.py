import sys

alphabet = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]

word = sys.stdin.readline().rstrip()

for a in alphabet:
    word = word.replace(a, "*")

print(len(word))
