N = int(input())

for n in range(N):
    S = list(map(str, input().split()))
    print(f"Case #{n+1}:", end=" ")
    
    for i in range(len(S)-1, -1, -1):
        print(S[i], end=" ")
        
    print("")