"""
시작 : 1: 55
0. 문제 이해
    - 입력 : 길이 N , 목표 이하 K
    - 출력 : 반복 수가 K개 이하인 연속한 slicing 중 최대 길이
    - 연속 부분 수열 이란?
        - 수열이 이어져있어야 함.
    - 숫자 범위
        - N : 2 e5
        - K : e2
        - a : e5
1. 아이디어
    - 완전탐색을 하기엔 N! 이라 어려움.
    - 투포인터
        - left = right = 0 시작
        - right 가 커지며 각 숫자의 출현 수 nd 에 더함
            - nd를 더할 때 K를 넘는 경우
                - 그 전까지 right - left + 1 을 maxn에 저장
        - 이후 nd.values의 max가 K 미만일 때까지 left 상승
            - 이후 반복
        -시간복잡도 2 N = 4 e5
"""
import sys
input = sys.stdin.readline

N, K = map(int,input().split())
nl = list(map(int,input().split()))

l = 0
r = 0

nd = {}
for d in set(nl):
    nd[d] = 0

f = nl[0] # 확인할 문제의 숫자, 처음엔 아무 값이나
nd[f] += 1

maxl = 0
while (l < N):
    if nd[f] <= K:
        print(f'l : {l}, r : {r}, f : {f}, nd[nl[r]] : {nd[nl[r]]}')
        if r == N-1:
            maxl = max(maxl, r - l+1)
            break
        r += 1

        nd[nl[r]] += 1

        if nd[nl[r]] > K: # 하나라도 초과할 경우
            f = nl[r]
            maxl = max(maxl, r-l)
    else :
        nd[nl[l]] -= 1
        l += 1

print(maxl)

