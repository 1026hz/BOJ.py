T = int(input())
for _ in range(T):
    H,W,N = map(int, input().split())
    num = N//H + 1 #호수
    floor = N%H #층
    if N%H == 0:
        num = N//H  #호수
        floor = H #층
    print(floor * 100 + num)