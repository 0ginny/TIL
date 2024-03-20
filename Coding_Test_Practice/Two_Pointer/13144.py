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
f = nl[0]
cnt = 0

"""
논리 다시 전개해
- 언제까지 돌꺼야? : l = r = last
- r은 언제 더해줘? r+1 까지 가면 문제가 생길 때까지
    - 그 때는 어떻게 돌아? l이 r과 같아질 때까지 돌아 
        - 같아지면 ? r, l = r+1로 바꿔줘.
        - 그리고 반복
"""

while l < N-1:
    print(f'l : {l}, r : {r}, cnt : {cnt}, nd : {nd}')
    if nd[nl[r+1]] < 1 :
        nd[nl[r]] += 1
        r += 1
    else :
        nd[nl[l]] -= 1
        l += 1
    cnt += 1
print(cnt)