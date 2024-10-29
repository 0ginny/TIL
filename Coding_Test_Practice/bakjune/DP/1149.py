'''
시작 :5:37

색 : 빨, 파 , 초
양옆 집이 같은 색이면 안돼.

각 집을 빨, 파, 초 로 색칠하는 비용이 적힘

최소 비용 출력

1. 구현방법
1개 일때 최소를 리스트에 저장
2개 일때,

'''

import sys
input = sys.stdin.readline


N = int(input())

price = [list(map(int,input().split())) for _ in range(N)]
# print(price)
min_price = [[0,0,0] for _ in range(N)]

for i in range(N):
    if i == 0 :
        min_price[i] = price[i]
    else :
        min_price[i][0] = min(min_price[i-1][1], min_price[i-1][2]) + price[i][0]
        min_price[i][1] = min(min_price[i-1][0], min_price[i-1][2]) + price[i][1]
        min_price[i][2] = min(min_price[i-1][1], min_price[i-1][0]) + price[i][2]

print(min(min_price[N-1]))