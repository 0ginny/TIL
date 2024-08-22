'''
시작 : 12:55

0. 문제 이해
- 창고 다각형의 면적이 가장 작은 창고를 만들기
비가 올 때 물이 고이지 않도록 지붕의 어떤 부분도 오목하게 들어간 부분이 없어야 한다.

- 입력 :
첫 줄에는 기둥의 개수를 나타내는 정수 N이 주어진다. N은 1 이상 1,000 이하
 N 개의 줄에는 각 줄에 각 기둥의 왼쪽 면의 위치를 나타내는 정수 L과 높이를 나타내는 정수 H

1. 아이디어
- 구현
(L,H) 로 리스트로 저장, 가장 높은 H 를 찾아 L 도 저장
L 이 순서대로 나열되지 않아. 일단 정렬 NlogN

오목한 부분이 없어야 하기에,
아래서 Max 까지, 맨 뒤에서 M 까지
이 과정 중 max * max 까지의 거리 의 합


'''

import sys

input = sys.stdin.readline

N = int(input())

tlist = [list(map(int,input().split())) for _ in range(N)]
tlist.sort(key = lambda x : x[0])

maxh = 0
maxl = 0
maxi = 0
maxd = 1 # 가장 높은 위치의 너비
maxdi = 1
for i, [l,h] in enumerate(tlist):
    if h > maxh :
        maxh = h
        maxl = l
        maxdi = 1
        maxd = 1
        maxi = i
    elif h == maxh :
        maxdi = i-maxi
        maxd = l - maxl

temph = 0
templ = 0
total = 0

for [l, h] in tlist[:maxi+1]:
    if temph == 0:
        templ = l
        temph = h
    else :
        if temph <= h :
            total += temph * (l- templ)
            templ = l
            temph = h
            # print(total,'up')
temph = 0
templ = 0
for [l, h] in tlist[:maxi+maxdi-2:-1]:
    if temph == 0:
        templ = l
        temph = h
    else :
        if temph <= h :
            total += temph * (templ- l)
            templ = l
            temph = h
            # print(total,'down')

total += maxh * maxd
print(total)