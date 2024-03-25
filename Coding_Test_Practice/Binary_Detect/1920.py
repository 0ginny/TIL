"""
시작 12:48
0. 문제 이해
    - 입력 :
        - 리스트 수
        - 리스트 숫자들
        - 테스트 수
        - 테스트할 숫자들
    - 출력 :
        - 리스트안에 테스트할 숫자가 있는지 : 있으면 :1 없으면 0 (테스트 수만큼 출력)
    - 숫자범위
        - 리스트 수 : e5
        - 검색 수 : e5
        - 정수범위 2^-31 ~ 2^31
1. 아이디어
    - if in : O(N)
        - N 번 반복 O(N^2) 안됨
    - 100000이면 nlogn을 쓰는 것이 좋음.
        -> 이분탐색
"""

import sys
input = sys.stdin.readline

N = int(input())
nl = list(map(int,input().split()))
M = int(input())
ml = list(map(int,input().split()))

nl.sort()
ans =[]
def binary(s,e,t):
    if s == e :
        if nl[s] == t:
            ans.append(1)
        else :
            ans.append(0)
        return

    mid = (s + e)//2
    if nl[mid] < t:
        binary(mid+1,e,t)
    else :
        binary(s,mid,t)

for m in ml:
    binary(0,N-1,m)
for a in ans:
    print(a)
