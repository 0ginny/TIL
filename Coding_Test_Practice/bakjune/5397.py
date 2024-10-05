'''
19:32

탐색기는 연결리스트로 풀 수 있어
'''

import sys
from collections import deque

input = sys.stdin.readline

t = int(input())
ans = []


def func(f):
    if f == '<':
        try:
            rq.appendleft(lq.pop())
        except :
            pass
    elif f == '>' :
        try :
            lq.append(rq.popleft())
        except :
            pass
    elif f == '-' :
        if lq :
            lq.pop()
    else :
        lq.append(f)


for _ in range(t):
    rq = deque([])
    lq = deque([])
    line = input().rstrip()
    for w in line:
        func(w)
    ans.append(''.join(lq+rq))
for a in ans:
    print(a)
