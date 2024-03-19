"""
시작 4:06
0. 문제 해석
    - 입력 : 행, 열, 목표깊이
    - 이미 간 곳은 가지 않음
    - T는 갈 수 없음
    - 출력 : 목표깊이의 가짓수
    - 시작 : [-1][0] / 끝 : [0][-1]

1. 아이디어
    - 깊이가 달라져? 재귀? 최대 4**25 불가능
    - 일단 해봐??


    - 찾아보니 시간복잡도는 3N 이래..
        백트래킹과 dfs의 차이가 뭘까??
"""

import sys
input = sys.stdin.readline

R,C,K = map(int,list(input().rstrip().split()))

road = [list(input().rstrip()) for _ in range(R)]

road[0][-1] = 'C'
road[-1][0] = 'T'

ans = 0

dx = [0,-1,0,1]
dy = [1,0,-1,0]

def rec(depth, y, x):
    # print(f'depth : {depth}, y : {y}, x : {x}')
    global ans
    #종료조건
    if depth == K:
        if (y == 0 ) and (x == C-1):
            ans += 1
        return
    #재귀
    for k in range(4):
        nx = x + dx[k]
        ny = y + dy[k]
        if (0 <= nx < C) and (0<= ny < R):
            if road[ny][nx] != 'T':
                road[ny][nx] = 'T'
                rec(depth+1,ny,nx)
                road[ny][nx] = '.'

rec(1,R-1,0)
print(ans)