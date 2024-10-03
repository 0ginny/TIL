'''14:09

bfs 인데 chk 가 최대 사탕 갯수야
시간복잡도 e6 가능
왜 시간 초과지??


'''

import sys
from collections import deque

input = sys.stdin.readline

H,W = map(int,input().split())

maze = [list(map(int,input().split())) for _ in range(H)]
maxc = [[0] * W for _ in range(H)]


di = [0, 1,1]
dj = [1,0,1]

q = deque([(0,0)])
maxc[0][0] = maze[0][0]


while q:
    i,j = q.popleft()
    for k in range(3):
        ni = i + di[k]
        nj = j + dj[k]

        if 0 <= ni <H and 0 <= nj < W :
            maxc[ni][nj] = max(maxc[i][j] + maze[ni][nj],maxc[ni][nj])
            q.append((ni,nj))

print(maxc[H-1][W-1])