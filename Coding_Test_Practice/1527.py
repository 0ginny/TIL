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


def tens(n): # 자릿수 구하는 함수
    return len(list(str(n)))

golds = []

def recul(s,t) : # t 자릿수 모든 금민수 저장
    if len(s) == t:
        global golds
        golds.append(s)
        return
    unit = ["4", "7"]
    for u in unit:
        ns = s + u
        recul(ns,t)

A_ten = tens(A)
B_ten = tens(B)

#가능한 모든 금민수 저장
for t in range(A_ten,B_ten+1):
    recul("",t)

cnt = 0
# 그중 범위 이상 금민수 숫자 확인
for g in golds:
    if not ( A <= int(g) <= B):
        cnt += 1
# 모든 금민수에서 cnt 수 빼기
print(len(golds) - cnt)
"""
2차 금민수 완전 탐색 후 범위 미 포함 제거로 성공
"""