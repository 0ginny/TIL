'''
시작 : 19:00


백트래킹 처럼 하면 될 듯
시간 초과

DP 에서 (n-1 /3 ,n/2)
'''

import sys
input = sys.stdin.readline

N = int(input())

dp = [0] * (N+1)

for i in range(2, N + 1):
    # 1을 뺀 경우
    dp[i] = dp[i - 1] + 1

    # 2로 나누어지는 경우
    if i % 2 == 0:
        dp[i] = min(dp[i], dp[i // 2] + 1)

    # 3으로 나누어지는 경우
    if i % 3 == 0:
        dp[i] = min(dp[i], dp[i // 3] + 1)

print(dp)