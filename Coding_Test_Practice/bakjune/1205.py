'''
시작 : 10:34
종료 : 11:17

... 질문게시판으로 반례 확인...
1 0 10
1
answer : 2

10 1 11
1 1 1 1 1 1 1 1 1 1
answer : 1

1. 아이디어
구현
- 랭크 리스트 저장
- P 만큼 for문 돌리기
    - N 보다 작은 경우
        - rank[i] < s 면 종료
        - rank[i] == s 라면
            - 만약 N < P 라면
'''

import sys

input = sys.stdin.readlineK


N, s, P = map(int,input().split())

if N > 0 :
    rank = list(map(int, input().rstrip().split()))
    for i in range(P):
        if i < N:
            if rank[i] < s:
                break
            else :
                if i == N-1 or i == P-1 :
                    if P <= N :
                        i = -2
                if rank[i] == s:
                    if rank[-1] != s:
                        break
        else:
            if rank[-1] > s :
                i = N
                break
            elif rank[-1] == s:
                i = rank.index(s)
                break
else :
    i = 0
print(i+1)