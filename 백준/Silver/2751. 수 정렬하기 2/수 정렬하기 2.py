import sys
N = int(sys.stdin.readline())
# pythonic code
lst = [int(sys.stdin.readline()) for i in range(N)]
lst.sort()
# enumerate() -> 파이썬 내장함수, lst를 반복하며 (인덱스,요소)쌍 반환
for i,v in enumerate(lst):
    print(v)