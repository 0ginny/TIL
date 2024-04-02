# MST

- minimum spanning tree
    - spanning tree
      - 모든 노드가 연결된 트리
    - 최소 비용으로 모든 노드가 연결된 트리
- 방법
  - kruskal
    - 전체 간선(가중치) 중 작은것부터 연결
    - union-find 알고리즘
    
  - prim
    - 현재 연결된 트리에 이어진 간선중 가장 작은것을 추가
    - **heap** 사용
      - 최소나 최대를 빠르게 찾을 수 있는 자료구조
      - 이진 트리 구조
      - 처음에 저장할 때부터 최대값이나 최소값을 저장하도록 결정해줘야함.

- 핵심코드
```python
heap = [[0,1]]

while heap :
    w, next_node = heapq.heappop(heap)
    if chk[next_node] == False:
        chk[next_node] = True
        rs += w
        for next_edge in dege[next_node]:
            if chk[next_edge[1]] == False:
               heapq.heappush(heap,next_edge)

```