while True:
    try:
        stringInput = input()

    except EOFError:
        break

    lower = 0
    upper = 0
    num = 0
    space = 0

    for i in range(len(stringInput)):
        if 97 <= ord(stringInput[i]) <= 122:
            lower += 1
        elif 65 <= ord(stringInput[i]) <= 90:
            upper += 1
        elif 48 <= ord(stringInput[i]) <= 57:
            num += 1
        elif stringInput[i] == " ":
            space += 1
        
    print(lower, upper, num, space)