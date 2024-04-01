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
import sys


n,s,a,b = 6,4,6,2
fares = [[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22], [1, 6, 25]]
road = []
def solution(n, s, a, b, fares):
    INF = sys.maxsize
    answer = INF
    road = [[] for _ in range(n+1)]
    for l in fares:
        road[l[0]].append([l[2],l[1]])
        road[l[1]].append([l[2], l[0]])

    heap = [[0,s]]

    fare = [INF] * (n+1)
    fare[s] = 0
    while heap :
        w, v = heapq.heappop(heap)
        if w > fare[v] :
            continue
        for nw, nv in road[v] :
            if fare[nv] > nw + w :
                fare[nv] = nw+ w
                heapq.heappush(heap,(fare[nv],nv))

    # 이중 최소 값 구하기
    for cv in range(1,n+1):
        answer = min(answer,fare[cv] )

    return fare


print(solution(n,s,a,b,fares))
