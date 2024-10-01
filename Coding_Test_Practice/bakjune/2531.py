'''
시작 : 00:37

목표는 최대로 먹을 수 있는 초밥 가지수

k 개의 초밥을 연속적으로 먹어
여기에 c 번호 초밥을 하나 더 추가

1. 아이디어
일단은 부루탈포스 가능?
30000
으로 가능하긴 해.

근데 슬라이싱이 불가해서 for 문으로 했더니 시간초과야.
투포인터로 가.
'''
from collections import deque
import sys

input = sys.stdin.readline

N, d, k, c = map(int,input().split())

rail = [int(input()) for _ in range(N)]
q = deque(rail[-k:])
maxt = 0
for i in range(N):
    q.popleft()
    q.append(rail[i])
    if c in q:
        temp = len(set(q))
    else :
        temp = len(set(q)) + 1
    maxt = max(temp,maxt)

print(maxt)
