"""
시작 : 2:32
1. 아이디어
    set(list(string)) 을 통해 금민수 판별
    - but 10억번을 하기엔 시간복잡도가 너무 높음.
        - 체크를 안할 수 있는 경우가 있나? 범위 자릿수를 고려해서 가장 높은 자리가 4와 7일 경우만 생각
        적어도 2억번으로 줄일 수 있음
        - 전체를 비교하기보단, 그냥 금민수인 걸 제공하면 되지 않을까?
            - 자릿수 : 10 자리
            - 각 자리별 금민수 4나 7
                - 범위만 주어지면 금민수 만들 수 있음. 최소 자리와 최대 자리를 생각하자.
    - 일단 완전 탐색으로 시도하고 가능한지 확인
"""

import sys
input = sys.stdin.readline

A,B = map(int,input().split())

cnt = 0

def chk(n):
    global cnt
    s = set(list(str(n)))
    # print(s)
    if s in [{'4','7'},{'7'},{'4'}]:
        cnt += 1

for n in range(A,B+1):
    chk(n)
print(cnt)

"""
1 차 시도 시간 초과
2 차는 범위를 줄여서 실행해보자.
"""