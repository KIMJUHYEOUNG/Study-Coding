import heapq

def dijkstra(start,end,n):
    q = []
    heapq.heappush(q,(0,start))
    distance = [INF] * (n+1)
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q,(cost, i[0]))
    print(distance[end])
    

INF = int(1e9)

n,m = list(map(int,input().split()))

graph = [[] for _ in range(n+1) ]

for _ in range(n-1):
    a,b,c = list(map(int,input().split()))
    graph[a].append((b,c))
    graph[b].append((a,c))
for _ in range(m):
    s,e = list(map(int,input().split()))
    dijkstra(s,e,n)
