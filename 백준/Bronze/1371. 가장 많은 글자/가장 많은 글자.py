import sys

S = sys.stdin.read()
alphabet = [0]*26

for i in S:
    if i.islower():
        alphabet[ord(i)-ord('a')] += 1

for j in range(26):
    if alphabet[j] == max(alphabet):
        print(chr(j+ord('a')), end="")