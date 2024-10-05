'''
시작 : 12:40

오름차순으로 주어지기에, 아래부터 동전을 쓰고 안되면 위로 가면 돼.
'''

import sys

input = sys.stdin.readline

N,K = map(int,input().split())

coins = [int(input()) for _ in range(N)]

ans = 0
for c in coins[::-1]:

    ans += K//c
    K %= c
    if K == 0 :
        break
print(ans)

