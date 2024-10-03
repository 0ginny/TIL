'''
시작 : 15:48

내리막으로만 가는 경로의 갯수를 구하기

dfs 보다 dp 로 하는 게 더 편할 듯, 왜냐하면 어차피 위에서 아래로만 갈 수 있어서 뒤로 가는 경우는 없어.
근데 그냥 전체 탐색으로 하면 뒤로 갈 때 더하는 순서가 달라서 문제가 틀려

'''


import sys

input= sys.stdin.readline

H, W = map(int,input().split())

m = [list(map(int,input().split())) for _ in range(H)]
dp = [[0] * W for _ in range(H)]

di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]
dp[0][0] = 1
q = [(0,0)]

for i in range(H):
    for j in range(W):
        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]
            if 0 <= ni < H and 0 <= nj < W :
                print(f' ni: {ni}, nj : {nj}, m[ni][nj] {m[ni][nj]}, m[i][j] : {m[i][j]}')
                if m[ni][nj] < m[i][j]:
                    dp[ni][nj] += dp[i][j]
print(dp)

