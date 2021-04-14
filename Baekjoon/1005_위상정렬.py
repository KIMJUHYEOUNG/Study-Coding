from collections import deque

t = int(input())
for _ in range(t):

    n,k = list(map(int,input().split()))

    build_time = list(map(int,input().split()))

    building = [0] * n
    graph = [[0]*n for _ in range(n)]
    degree = [0] * n
    
    for i in range(n):
        building[i] = build_time[i]
    tech = []

    for i in range(k):
        a,b = list(map(int,input().split()))
        a -= 1; b -= 1
        tech.append([a,b])
        graph[a][b] = 1
        degree[b] += 1
    que = deque([])
    for i in range(n):
        if degree[i] == 0:
            que.append(i)
    while que:
        idx = que.popleft()
        for i in range(n):
            if graph[idx][i]:
                degree[i] -= 1
                building[i] = max(building[idx]+build_time[i], building[i])
                if degree[i] == 0:
                    que.append(i)
    
    l = int(input())
    print(building[l-1])
