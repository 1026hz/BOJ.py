X = int(input())
stick = [64]

while True:
    if X == sum(stick):
        break
    
    stick[-1]=stick[-1]/2
    if sum(stick)<X:
        stick.append(stick[-1])
    
print(len(stick))