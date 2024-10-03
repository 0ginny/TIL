'''14:09

bfs 인데 chk 가 최대 사탕 갯수야
시간복잡도 e6 가능
왜 시간 초과지??

그냥 dp로 가자

'''

import sys

input = sys.stdin.readline

H,W = map(int,input().split())

maze = [[0]* (W+1)] +[[0] +list(map(int,input().split())) for _ in range(H)]

print(maze)
dp = [[0] * (W+1) for _ in range(H+1)]

for i in range(1,H+1):
    for j in range(1,W+1):
        dp[i][j] = max(dp[i-1][j-1] + maze[i][j]+maze[i][j-1],
                       dp[i-1][j-1] + maze[i][j]+maze[i-1][j],
                       dp[i-1][j] + maze[i][j],
                       dp[i][j-1] + maze[i][j])

print(dp[H][W])