A = input()
lst = [i for i in A]

while (A != '#'):

    if A[-1] == 'e':
        if A.count('1') % 2 == 0:
            lst[-1] = '0'
        else:
            lst[-1] = '1'

    else:
        if A.count('1') % 2 == 0:
            lst[-1] = '1'
        else:
            lst[-1] = '0'

    print(*lst, sep="")

    A = input()
    lst = [i for i in A]