'''
시작 : 15:28

항상 현재 칸에 적혀있는 수만큼 오른쪽이나 아래로 가야 한다.
한 번 점프를 할 때, 방향을 바꾸면 안 된다.
경로의 개수를 구하는 프로그램

dp 로 가능한 이유는
가로줄로 다 실행을 해도 다음 차례에 영향을 주지 않기 때문이야 .위, 오른쪽으로만 가니까
'''

import sys

input= sys.stdin.readline

n = int(input())
jump = [list(map(int,input().split())) for _ in range(n)]
dp = [[0]*n for _ in range(n)]

dp[0][0] = 1

di = [0,1]
dj = [1,0]
for i in range(n):
    for j in range(n):
        d = jump[i][j]
        if d != 0:
            for k in range(2):
                ni = i + d * di[k]
                nj = j + d * dj[k]
                if ni < n and nj < n :
                    dp[ni][nj] += dp[i][j]
print(dp[-1][-1])