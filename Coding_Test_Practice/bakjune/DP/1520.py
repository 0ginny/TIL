'''
시작 : 15:48

내리막으로만 가는 경로의 갯수를 구하기

dfs 보다 dp 로 하는 게 더 편할 듯, 왜냐하면 어차피 위에서 아래로만 갈 수 있어서 뒤로 가는 경우는 없어.
근데 그냥 전체 탐색으로 하면 뒤로 갈 때 더하는 순서가 달라서 문제가 틀려
dfs 로 해야하나봐- 시간 초과 안나올까? 일단 뒤로 갈 수는 없어. 모든 경우를 다 하는 거긴 해, N*M 가능할듯
아니네,, 시간초과네...

dp 의 특성을 이용해야해. 이단 작은 그룹부터 어떻게 할지 생각해

재귀 한도를 높여줘야 할 때도 있네..

'''


import sys
sys.setrecursionlimit(10**8)  # 재귀 한도 늘리기
input= sys.stdin.readline

H, W = map(int,input().split())

m = [list(map(int,input().split())) for _ in range(H)]
dp = [[0] * W for _ in range(H)]
chk = [[False]* W for _ in range(H)]

di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]
q = [(0,0)]
dp[0][0] = 1
chk[0][0] = True
def dfs(i,j):
    if chk[i][j] == False:
        chk[i][j]=True
        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]
            if 0 <= ni < H and 0 <= nj < W :
                if m[ni][nj] > m[i][j]:
                    dp[i][j] += dfs(ni,nj)
    return dp[i][j]

for i in range(H):
    for j in range(W):
        dp[i][j] = dfs(i,j)
print(dp[-1][-1])

