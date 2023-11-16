import sys
A = list(map(int, sys.stdin.readline().split()))
burger = sorted(list(map(int, sys.stdin.readline().split())), reverse=True)
side = sorted(list(map(int, sys.stdin.readline().split())), reverse=True)
coke = sorted(list(map(int, sys.stdin.readline().split())), reverse=True)

discount = (sum(burger[:min(A)]) + sum(side[:min(A)]) + sum(coke[:min(A)]))*0.9

if len(burger) > min(A):
    discount += sum(burger[min(A):])

if len(side) > min(A):
    discount += sum(side[min(A):])

if len(coke) > min(A):
    discount += sum(coke[min(A):])

print(sum(burger)+sum(side)+sum(coke))
print(int(discount))
