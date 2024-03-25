"""
시작 : 6:57
0. 문제이해
    - 무지와 어피치가 귀가를 하며 가장 적은 비용
    - 문제조건
        - v : 3 ~ 200
        - e : n^2 /2 20000
1. 아이디어
    - mst로 풀면 될 거 같아
    - 근데 어피치와 무지가 같이 가는 곳의 무게는 반으로 줄여야해.
        - 시작 지점은 정해져 있어.
        - 중간 지점을 정해서 그곳에서 mst 2번을 진행, 총 3번의 mst를 진행해야해.



"""

import heapq



def mst(s,d) :
    heap = [[0, s]]

    while heap:  # heap이 빌때까지 반복
        w, en = heapq.heappop(heap)
        if chk[each_node] == False:  # 최소 가중치의 노드가 지나지 않았을 경우만
            chk[each_node] = True
            rs += w
            for next_edge in edge[each_node]:  # 해당 노드의 모든 간선을 힙에 추가가            if chk[next_edge[1]] ==False :
                heapq.heappush(heap, next_edge)



road = []
def solution(n, s, a, b, fares):
    answer = 0
    road = [] * (n+1)
    for l in fares:
        road[l[0]].append([l[2],l[1]])
        road[l[1]].append([l[2], l[0]])

    heap = [[0,s]]

    return answer


