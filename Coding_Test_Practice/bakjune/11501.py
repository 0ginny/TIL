'''
시작 : 17:36

0. 문제이해
매일 그는 아래 세 가지 중 한 행동을 한다.
    주식 하나를 산다.
    원하는 만큼 가지고 있는 주식을 판다.
    아무것도 안한다.
 날 별로 주식의 가격을 알려주었을 때,
    최대 이익이 얼마나 되는지 계산을 해달라고 부탁했다.

입력 :
테스트 수 T
일자 : D
각 일자별 주가

출력 : 최대 이익

1. 아이디어
치팅방지로 삭제하고 커밋함.

'''

import sys

input = sys.stdin.readline

T = int(input())
ans = []
for _ in range(T):
    maxp = 0
    total = 0
    _ = input()
    dlist = list(map(int,input().split()))
    for d in dlist[::-1]:
        if maxp < d :
            maxp = d
        else :
            total += maxp - d
    ans.append(total)

for a in ans:
    print(a)
