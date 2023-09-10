L = int(input())
word = input()
abc_list = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n",
            "o","p","q","r","s","t","u","v","w","x","y","z"]
ans = 0
for i in range(len(word)):
    ans +=(abc_list.index(word[i])+1)*(31**i)
print(ans)