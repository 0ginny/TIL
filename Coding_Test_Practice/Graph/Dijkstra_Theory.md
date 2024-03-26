# 다익스트라

- 한 노드 기준 다른 모든 노드까지 가는데 드는 각각의 최소비용
- 작동원리
  - 간선(인접리스트, 거리배열) : 초기값 무한대, 힙으로 시작점 추가
    - [inf, inf, inf ---] 이런식으로 처음에 넣어
    - 힙에 추가되면 최소 거리를 거리 배열 초기화
      - 추가되면 거리 갱신 및 힙에 추가

```
dist[K] = 0
heapq.heappush(heap,(0,K))

while heap:
  w,v = heapq.heappop(heap)
  if w!= dist[v] : continue
  for nw, nv in edge[v] +nw:
  dist[nv] = dist[v] + nw
  heapq.heappush(heap,(dist[nv],nv))
```