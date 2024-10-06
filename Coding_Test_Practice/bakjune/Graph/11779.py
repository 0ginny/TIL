'''
20:53

일단 시작도시릅 푸시해 푸시 할 때 (w, s, [])

'''

import sys
import heapq
INF = sys.maxsize
input = sys.stdin.readline

h = []

N = int(input())
T = int(input())
bs = [[] for _ in range(N+1)]
for _ in range(T):
    a,b,w = map(int,input().split())
    bs[a].append((w,b))

S,E = map(int,input().split())
dist = [INF] * (N+1)
ls = [[] for _ in range(N+1)]

h = [(0,S)]
dist[S] = 0
ls[S] = [S]
while h :
    w, n = heapq.heappop(h)
    # print(ls[n])
    if dist[n] >= w :
        for ww,b in bs[n]:
            if dist[b] > w + ww :
                dist[b] = w + ww
                ls[b] = ls[n] + [b]
                heapq.heappush(h,(w+ww,b))
print(dist[E])
ls[E].sort()
print(len(ls[E]))
print(' '.join(list(map(str,ls[E]))))


