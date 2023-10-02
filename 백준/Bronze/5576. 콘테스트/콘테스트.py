W = []
K = []

for _ in range(10):
    W.append(int(input()))
    
for _ in range(10):
    K.append(int(input()))

print(sum(sorted(W, reverse=True)[:3]),
      sum(sorted(K, reverse=True)[:3]))