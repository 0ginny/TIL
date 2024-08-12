'''
시작 : 10 : 36
종료 : 10 : 50
0. 문제 이해

사람들은 자신의 위치에서 거리가 K 이하인 햄버거를 먹을 수 있다.

입력 :
N, K : 식탁길이 , 햄버거 선택 거리
1<= N <= 20000
1<= K <= 10

둘째줄 햄버거와 사람 위치 (H 햄버거, P 사람)

출력 :
최대 몇명이 햄버거 먹을 수 있는지

1. 아이디어
그리디같아.

앞사람이 앞쪽부터 햄버거를 먹고 쭉 지나가면 될 거 같아.

- 햄버거 사람 리스트 작성
    - for h 문 :
        prelist append(h)
        if h == P :
            for range(i-K, i+K+1)
                if list[j] == H
                    list[j] = P
                    cnt += 1
                    break
    print(cnt)

- 시간복잡도 20000 * 20 가능
'''

import sys

input = sys.stdin.readline

N, K = map(int,input().split())
hlist = list(str(input().rstrip()))

cnt = 0
for i,h in enumerate(hlist):
    if h == 'P':
        for j in range(max(0,i-K),min(i+K+1,N)):
            if hlist[j] == 'H':
                hlist[j] = 'X'
                cnt += 1
                break

print(cnt)
