'''
시작 : 1745

0. 문제이해

지도가 주어지면 모든 지점에 대해서 목표지점까지의 거리를 구하여라.

문제를 쉽게 만들기 위해 오직 가로와 세로로만 움직일 수 있다고 하자.

-입력
지도의 크기 n과 m이 주어진다. n은 세로의 크기, m은 가로의 크기다.(2 ≤ n ≤ 1000, 2 ≤ m ≤ 1000)
0은 갈 수 없는 땅이고 1은 갈 수 있는 땅, 2는 목표지점이다.

- 출력
각 지점에서 목표지점까지의 거리를 출력한다.
    원래 갈 수 없는 땅인 위치는 0
    원래 갈 수 있는 땅인 부분 중에서 도달할 수 없는 위치는 -1


1. 아이디어
- bfs
    - 2 에서 시작
        해당 위치에서 갈 수 있는 모든 곳 ans[ni][nj] = ans[i][j] +1


'''

import sys
from collections import deque

input = sys.stdin.readline

H, W = map(int,input().split())

maplist = [list(map(int,input().split())) for _ in range(H)]
chk = False
for i in range(H):
    for j in range(W):
        if maplist[i][j] == 2 :
            # print(i,j)
            chk = True
            break
    if chk == True :
        break
# print(maplist)
di = [-1,0,1,0]
dj = [0,-1,0,1]

ans = [[0]* W for _ in range(H)]
q = deque([(i,j)])
# print(q)
# print(ans)
while q:
    (i, j) = q.popleft()
    for k in range(4):
        ni = i + di[k]
        nj = j + dj[k]

        if 0 <= ni < H and 0 <= nj < W :
            if maplist[ni][nj] == 1:
                if ans[ni][nj] == 0 :
                    ans[ni][nj] = ans[i][j] + 1
                    q.append((ni,nj))
                    # print(ans)

for line in ans:
    print(' '.join(list(map(str,line))))
