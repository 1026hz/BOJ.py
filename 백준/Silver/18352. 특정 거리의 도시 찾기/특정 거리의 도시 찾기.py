import sys
import heapq
input = sys.stdin.readline
INF = int(1e9)

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start]=0
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

n,m,k,start = map(int, input().split())
graph = [[] for _ in range(n+1)]
distance = [INF] * (n+1)

for i in range(m):
    a, b = map(int, input().split())
    graph[a].append([b,1])

dijkstra(start)
ans = []

for j in range(n+1):
    if distance[j] == k:
        ans.append(j)

ans = sorted(ans)
if len(ans):
    print(*ans, sep="\n")
else:
    print(-1)