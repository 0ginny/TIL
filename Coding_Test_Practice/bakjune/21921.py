'''
시작: 11:09
종료 : 11:21

0. 문제이해
가장 많이 들어온 방문자 수와 기간이 몇 개 있는지 구해주자.

- 입력
첫째 줄에 블로그를 시작하고 지난 일수 N 과 X
둘째 줄에는 블로그 시작 1일차부터 N일차까지 하루 방문자 수

-출력
첫째 줄에 X일 동안 가장 많이 들어온 방문자 수를 출력
    -단 최대가 0명이면 SAD
만약 0명이 아닌경우 그런 기간이 몇개 있는지 출력

1. 아이디어
- 구현
가장 쉬운건 전체를 다 나눠서 하는 건데 투포인터로 가자
    이렇게 해도 시간초과
        - deque로 하면 안되네
투 포인터로 가면서 최대를 리뉴얼 하고,
    - 최대가 리뉴얼 되면 cnt = 1
    - 동일하다면 cnt += 1
만약 최대가 0 이면 SAT 만 출력
'''

import sys
from collections import deque

input = sys.stdin.readline

N, X  = map(int,input().split())
plist = list(map(int,input().rstrip().split()))

maxp = 0
sump = 0
cnt  = 0
for i, n in enumerate(plist):
    if i < X:
        sump += n
        if i == X-1:
            maxp = sump
            cnt = 1
    else:
        sump -= plist[i-X]
        sump += n
        if maxp < sump:
            maxp = sump
            cnt = 1
        elif maxp == sump:
            cnt += 1

if maxp != 0:
    print(maxp)
    print(cnt)
else :
    print('SAD')
