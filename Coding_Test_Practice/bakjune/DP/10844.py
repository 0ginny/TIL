'''13:46

출력 e9로 나눈 나머지

인접한 조건이기 때문에 자릿수가 변했을 때 dp를 쓸 수 있는 거야
0부터 시작하면 계단 수가 아니야
'''

n = int(input())

dp = [[0] * 10 for _ in range(101)]

dp[1] = [1] * 10
for  i in range(2,n+1):
    dp[i][0] = dp[i-1][1]
    dp[i][9] = dp[i-1][8]

    for j in range(1,9):
        dp[i][j] = dp[i-1][j-1]+dp[i-1][j+1]

print(sum(dp[n][1:]) % 1000000000)