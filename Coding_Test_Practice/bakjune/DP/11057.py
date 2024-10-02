'''
22:30
'''

n = int(input())

dp = [[] for _ in range(1001)]

dp[1] = [1]* 10
# print(dp)
for i in range(2,n+1):
    temp = sum(dp[i-1])
    dp[i].append(temp)
    for j in range(1,10):
        temp -= dp[i-1][j-1]
        dp[i].append(temp)

print(sum(dp[n])%10007)
