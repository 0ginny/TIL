'''
시작 : 11:28
종료 : 11:45

문제를 똑바로 이해해.
일단 하나의 색을 고르면 그것만 이동시켜야해. 일단 2가지 케이스가 있겠지,
    근데 여기서 또 왼쪽으로 옮길지 오른쪽으로 옮길지 2가지 케이스가 있을거야.
한번에 하나씩만 옮길 수 있어.

1. 아이디어
그리디? 이상하면 그리디인데,
부루탈포스 가능? 4가지 케이스 N 500000

가능하네

그럼 일단 4가지 케이스로 이동을 시키고 최소 값을 구하면 됨.

'''

import sys

input = sys.stdin.readline

N = int(input())
balls = list(input().rstrip())

minc = sys.maxsize

# 왼쪽 블루, 블루이동
chk = False
cnt = 0
for b in balls:
    if b == 'R':
        chk = True
    if chk:
        if b == 'B':
            cnt += 1

minc = min(cnt,minc)

# 왼쪽 블루, 레드이동
chk = False
cnt = 0
for b in balls[::-1]:
    if b == 'B':
        chk = True
    if chk:
        if b == 'R':
            cnt += 1

minc = min(cnt,minc)

# 왼쪽 레드, 블루이동
chk = False
cnt = 0
for b in balls[::-1]:
    if b == 'R':
        chk = True
    if chk:
        if b == 'B':
            cnt += 1

minc = min(cnt,minc)

# 왼쪽 레드, 레드이동
chk = False
cnt = 0
for b in balls:
    if b == 'B':
        chk = True
    if chk:
        if b == 'R':
            cnt += 1

minc = min(cnt,minc)

print(minc)