from collections import deque
import sys
input = sys.stdin.readline

n,m = list(map(int,input().split()))

graph = [ [] for _ in range(n) ]

for _ in range(m):
    x,y = list(map(int,input().split()))
    graph[y-1].append(x-1)

result = []
mmax = 0
for i in range(n):
    que = deque([i])
    visit = [0] * n
    cnt = 0
    while que:
        k = que.popleft()
        visit[k] = 1
        cnt += 1
        for j in graph[k]:
            if visit[j] == 0:
                visit[j] = 1
                que.append(j)
    if mmax < cnt:
        result.clear()
        result.append(i)
        mmax = cnt
    elif mmax == cnt:
        result.append(i)

for i in result:
    print(i+1,end=" ")
