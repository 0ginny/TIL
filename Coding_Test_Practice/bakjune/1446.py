'''
시작 : 17:58

문제 이해
지름길 최소 거리
만약 시작 지점이 없으면 그냥 가야해

1. 아이디어
- 지름길이 있으면 쓰는 것이 맞아. 아니지 실제 길이보다 작은지 정도는 파악하자
- 일단 도착지점이 목표 지점보다 큰 지름길은 제외
- 일단 부루탈포스로 가야해
    - 지름길 쓰고, 그 이후 지름길을 쓰고 도착했을 때를 골라
        - 일단 시작지점으로 정렬을 해야할 듯
        - 사용 지름길 이후 인덱스 부터 시작해서 시작 지점 뒤에 있는 지름길을 사용했을 때 최종 거리 구하기
        - 맥스를 리뉴얼
    - 지름길 사용했으면 다시 되돌아오기
'''

import sys

input = sys.stdin.readline

N, L = map(int, input().split())

load = []
for _ in range(N):
    s,e,l = map(int,input().split())
    if e <= L :
        load.append([s,e,l])

load.sort(key = lambda x : x[0])
ll = len(load)
minl = 10000

def ref(idx,end,l):
    # print(f'idx : {idx}, end : {end}, l : {l}')
    for i in range(idx,ll):
        tl = l
        j = load[i]
        if end <= j[0]:
            tl += j[0]-end

            if j[2] < j[1] - j[0]:
                tl += j[2]
                ref(idx+1,j[1],tl)


    global minl
    minl = min(minl,l+ L - end)
    # print(f'min : {minl}')

ref(0,0,0)

print(minl)