"""
시작 : 8:38
홀수는 홀수끼리 짝수는 짝수끼리
그냥 바꾸면 되나?

- 일단 % 를 이용해서 1과 0인 집단으로 만들어.
- 1011010110 이런 걸 생각해봐
    - 옮기는게 적은 것이 항상 옳은가? 그건 또 아닐 수 있어.
    - 총 4가지 경우가 있어. 각각 최초-기준 까지의 거리의 합이야. 4개중 하나만 선택하며 되긴해.
    - 모든 경우를 다 고려하자.
"""

import sys
input = sys.stdin.readline

n = int(input())
chk = list(map(lambda x : int(x) % 2, input().split() ))

cnt = [0] * 4
case = [0]* 4 # 0왼, 0오, 1왼, 1오

for i in range(n):
    if chk[i] :
        case[2] += i - cnt[2]
        cnt[2] += 1
        case[3] += n -1 - i - cnt[3]
        cnt[3] += 1
    else :
        case[0] += i - cnt[0]
        cnt[0] += 1
        case[1] += n -1 - i - cnt[1]
        cnt[1] += 1

print(min(case))