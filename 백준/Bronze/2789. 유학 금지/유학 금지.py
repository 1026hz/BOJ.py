CAMBRIDGE = "CAMBRIDGE"
word = input()

i=0

while True:
    if i >= len(CAMBRIDGE):
        break

    if CAMBRIDGE[i] in word:
        word = word.replace(CAMBRIDGE[i],"")

    i+=1

print(word)