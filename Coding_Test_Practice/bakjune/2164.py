'''
시작 : 9:55
종료 : 10:05

0.문제이해
N장의 카드가 1번 카드가 제일 위에, N번 카드가 제일 아래인 상태로 순서대로 카드가 놓여 있다.
제일 위에 있는 카드를 바닥에 버린다. 그 다음, 제일 위에 있는 카드를 제일 아래에 있는 카드 밑으로 옮긴다.
N이 주어졌을 때, 제일 마지막에 남게 되는 카드를 구하는 프로그램을 작성

-입력
정수 N(1 ≤ N ≤ 500,000)이 주어진다.

-출력 : 마지막 카드 번호

1. 아이디어
구현인데 N이 500000이면 500000 + 2500000 +125000 --- 이런식으로 가
시간복잡도 e6 가능하긴해
그럼 쉽게 가자
'''

import sys
from collections import deque


input = sys.stdin.readline

N = int(input())

nlist = range(1,N+1)
q = deque(nlist)

cnt = False
while len(q) > 1:
    n = q.popleft()
    if cnt :
        q.append(n)
    cnt = not cnt

print(q[0])