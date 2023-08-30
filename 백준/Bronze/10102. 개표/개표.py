V = int(input())
choice = input()
A=0
B=0
for i in range(V):
    if choice[i] == 'A':
        A+=1
    elif choice[i] == 'B':
        B+=1
if A>B:
    print('A')
elif A<B:
    print('B')
else:
    print('Tie')