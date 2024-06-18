'''
1. 해결방법
- 깊이 3의 dfs 최대인 것 2번, 그리고 ,chk 순서 바꿔서 2번.

2. 시간복잡도
- 4**3*3*2 < 2*9 가능

'''

import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())

berries = [list(map(int, input().split())) for _ in range(N)]

starts = [list(map(lambda x: int(x) - 1, input().split())) for _ in range(M)]

chk = [[False] * N for _ in range(N) ]


q = deque()
sum = 0

di = [1,0,-1,0]
dj = [0,1,0,-1]
def dfs(n,temp):
    global sum, final
    if n == 3 :
        if temp > sum :
            final = chk.copy()

    i, j = q.pop()
    for k in range(4):
        ni = i + di[k]
        nj = j + dj[k]

        if 0 < ni < N and 0 < nj < N :
            if chk[ni][nj] == False:
                chk[ni][nj] = True
                q.append((ni,nj))
                temp += berries[ni][nj]
                dfs(n+1, temp)
                chk[ni][nj] = False
                temp -= berries[ni][nj]

for i in range(M):
    sum = 0
    dfs(0)