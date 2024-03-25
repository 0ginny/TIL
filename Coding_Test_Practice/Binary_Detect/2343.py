"""
시작 : 1: 57
0. 문제이해
    - 강의 순서가 바뀌면 안돼. (정렬하면 안됨)
    - 같은 크기 M개의 블루레이를 최소갯수로
    - 최소 블루레이 크기 출력
    - 입력 :
        - 강의수 N, 가진 블루레이 수 M
        - 강의 리스트 nl
    - 출력 :
        - 각각 강의를 합칠 최소의 블루레이 길이
    - 숫자 범위
        - N  e5
        - 1<= M <= N
        - 강의시간 < 10000
1. 아이디어 :
    - 블루레이 크기 가정
        - 최대 크기가 e9 니까 불가능
    - 블루레이 길이 이분탐색
        - lnN * N(다 더해서 판별) + NlnN (정렬) (X) 정렬을 하면 안됨. 문제 조건.
"""

import sys
input = sys.stdin.readline

N, M = map(int,input().split())
nl = list(map(int,input().split()))

s,e = max(nl), max(nl) * N

def chk(t):
    cnt = 0
    temp = 0
    for n in nl:
        temp += n
        if temp > t:
            temp = n
            cnt += 1
        if temp == t:
            temp = 0
            cnt += 1
    if temp > 0 :
        cnt += 1
    return cnt

while s < e :
    mid = (s+e) //2
    c = chk(mid)
    # print(f' s: {s} , e : {e}, mid : {mid}, cnt : {c}')

    if c > M :
        s = mid+1
    else :
        e = mid
print(e)

"""
이분탐색에서 고려할 것
    - 정렬 여부
    - start와 end 값 ★★★★★★★★
    - 출력값
    - 어떤 걸 기준으로 탐색할 건지.
"""