X, Y = map(str, input().split())
revX = int(X[::-1])
revY = int(Y[::-1])
print( int(str(revX + revY)[::-1]) )