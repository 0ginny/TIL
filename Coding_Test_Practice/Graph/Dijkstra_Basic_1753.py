import sys
import heapq

input = sys.stdin.readline

V, E = map(int,input().split())
S = int(input())
el = [[] for _ in range(V+1)]

for _ in range(E) :
    a,b,c = map(int,input().split())
    el[a].append((c,b))

INF = sys.maxsize
dist = [INF] * (V+1)

# 시작점 초기화화
dist[S] = 0
heap = [[0,S]]

while heap :
    w, v = heapq.heappop(heap)
    if w != dist[v] :
        continue
    for nw, nv in el[v]:
        if dist[nv] > nw + w :
            dist[nv] = nw + w
            heapq.heappush(heap,(dist[nv],nv))
for i in range(1,len(dist)) :
    if dist[i] == INF :
        print('INF')
    else :
        print(dist[i])

