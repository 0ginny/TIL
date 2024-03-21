"""
시작 : 2: 55
0. 문제 이해
    - 연속한 1개 이상의 수를 뽑을 때야
        - 1개씩 뽑을 때 겹치지 않는 수 +
        - n개씩 뽑을 때 겹치지 않는 수
    - 입력 : N : e5
    - 출력 : 경우의 수
1. 아이디어 :
    - 완전탐색
        - N! 불가능
    - 투포인터
        - left, right = 0, 0
        - right 올라가며
            - 해당 위치 숫자 추가 nd += 1
                (nd 는 숫자 나온 횟수 찾는 딕셔너리)
            - 연속된 수 있는지 확인
                -있으면 left 상승
            - r이 커질 때마다 cnt += 1
"""

import sys
input = sys.stdin.readline

N = int(input())
nl = list(map(int,input().split()))

nd = {}
for d in set(nl):
    nd[d] = 0

l , r = 0 , 0

cnt = 0

"""
논리 다시 전개해
- 삼각수 같은 거야. 팩토리얼을 구현하려면 r-l을 해주면 돼.
- 언제까지?
    r = l = last
- 언제 숫자 더해?
    - r 이 두번 나오기 전까지 올라가면서 
        - l이 r의 수가 0이 될 때까지 올라가면서 
    - r = l = last면 종료 

1 2 3 2 4 5 3 를 생각해보자

"""

while r < N :
    # print(f'l : {l}, r : {r}', end = '\t')
    if nd[nl[r]] < 1 :
        nd[nl[r]] += 1
        r += 1
        cnt += r - l
    else:
        while nd[nl[r]] == 1:
            nd[nl[l]] -= 1
            l += 1

    # print(f' cnt : {cnt}, nd : {nd}')
print(cnt)