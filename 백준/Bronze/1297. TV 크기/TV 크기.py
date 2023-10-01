import math

D,H,W = map(int,input().split())

n = D**2 / (H**2 + W**2)
num = math.sqrt(n)

print(int(H*num), int(W*num))