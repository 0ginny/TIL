'''
19:44

최소 비용

dp[i] = min(dp[i],dp[k] + c[k][i])

일단 최초는 각각에 물을 대는 것.
    그 후

'''

import sys
import heapq

input = sys.stdin.readline

N = int(input())
h = []
for i in range(N):
    cost = int(input())
    heapq.heappush(h,(cost,i))
INF = sys.maxsize
cs = [list(map(int,input().split())) for _ in range(N)]
ans = [INF] * N
chk = [False] * N
while h :
    (w, n) = heapq.heappop(h)
    if ans[n] > w :
        ans[n] = w
        # print(f'n : {n}, w {w}, ans {ans}, heap {h}')
        chk[n] = True
        for i in range(N):
            if i != n :
                if chk[i] == False:
                    if ans[i] > cs[n][i]:
                        heapq.heappush(h,(cs[n][i],i))
print(sum(ans))