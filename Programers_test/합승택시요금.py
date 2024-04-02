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

INF = sys.maxsize
n,s,a,b = 6,4,6,2
fares = [[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22], [1, 6, 25]]
road = []



def solution(n, s, a, b, fares):
    INF = 200* 100000 + 1
    answer = INF
    road = [[] for _ in range(n)]
    for l in fares:
        road[l[0]-1].append([l[2],l[1]-1])
        road[l[1]-1].append([l[2],l[0]-1])

    #daijstra algorithm
    def dijstra(s):
        heap = [[0, s]]

        fare = [INF] * n
        fare[s] = 0
        while heap:
            w, v = heapq.heappop(heap)
            if w > fare[v]:
                continue
            for nw, nv in road[v]:
                if fare[nv] > nw + w:
                    fare[nv] = nw + w
                    heapq.heappush(heap, (fare[nv], nv))
        return fare

    fl = [dijstra(i) for i in range(n)]

    # answering
    for vvv in range(n):
        # print(f' v : {vvv}, answer : {answer}, {fl[s][vvv]} + {fl[vvv][a]} + {fl[vvv][b]}')
        answer = min(fl[s-1][vvv] + fl[vvv][a-1] + fl[vvv][b-1], answer)

    return answer


print(solution(n,s,a,b,fares))
