'''
22:46


1. dp
dp[i] = 1  + dp[-2] + int(i/2)

'''

import sys

input = sys.stdin.readline

T = int(input())
test = [int(input()) for _ in range(T)]

maxt = max(test)

dp = [0] * (maxt + 1)

dp[1] = 1
dp[2] = 2
dp[3] = 3

for i in range(4,maxt+1):
    dp[i] = 1 + dp[i-3] + int(i/2)

for a in test:
    print(dp[a])
