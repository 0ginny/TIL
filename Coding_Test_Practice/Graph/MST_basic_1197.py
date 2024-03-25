# 보통 mst 는 양방향 그래프

"""
- 간선을 인접 리스트 형태로 저장 :: [(w,v),(),(),()]
- 시작점 힙에 넣기
- 힙이 빌때까지
    - 해당 노드 방문 안한 곳일경우
    - 방문 체크, 비용 추가, 연결된 간선 새롭게 추가

-시간복잡도 : ElogE
    - edge 리스트 저장 : E
    - heqp 안의 모든 edge에 연결된 간선 확인 : E+ E
    - 힙 삽입 E * logE
"""

import sys
import heapq
input = sys.stdin.readline

V,E = map(int, input().split())
edge = [[] for _ in range(V+1)]
chk = [False] * (V+1)
rs = 0
for i in range(E):
    a,b,c = map(int, input().split())
    edge[a].append([c,b])
    edge[b].append([c,a])

heap = [[0,1]] # V가 최소 1이니까 1은 반드시 있으니.

while heap: # heap이 빌때까지 반복
    w, each_node = heapq.heappop(heap)
    if chk[each_node] == False: #최소 가중치의 노드가 지나지 않았을 경우만
        chk[each_node ] = True
        rs += w
        for next_edge in edge[each_node]: #해당 노드의 모든 간선을 힙에 추가가            if chk[next_edge[1]] ==False :
                heapq.heappush(heap, next_edge)