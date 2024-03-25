"""
시작 : 1:27
0. 문제 분석
    - 입력 :
        - 지방의 수 N
        - 지방 예산 요청값들 nl
        - 총예산 (한계) M
    - 출력 :
        - 최대 상한선 :: 이 수 이상인 것은 상한선으로 통일, 그렇게 합쳐서 총예산을 넘지않는 최대
    - 수범위
        - N 3~10000
        - 요청값 : 100000
        - 총예산 N ~ e9
1. 아이디어 :
    - 최악 : nl 의 최솟값과 최대값 사이의 상한선을 가정하고 M을 넘지않는 최대 수를 고려
        - e10 불가능
    - 숫자가 100000개니 이진탐색을 고려해보자.
        - 가운데 숫자를 상한선으로 해서 값이 넘으면 더 작은 범위로
            -높으면 더 적은 범위로
        - 언제 종료?
            - s == e 인 경우
            - 마지막 숫자의 소숫점 내림값.
"""
import sys
input = sys.stdin.readline

N = int(input())
nl = list(map(int,input().split()))
M = int(input())

minn = min(nl)
maxn = max(nl)

def define(up):
    total = 0
    for n in nl:
        if n >= up:
            total += up
        else :
            total += n
    return total


def binary(s,e,t):

    mid =  (s+e) //2
    total = define(mid)
    # print(f's : {s}, e : {e}, mid : {mid}')
    if  s == e :
        if total > t :
            print(e-1)
            return
        else :
            print(e)
            return

    # print(f's : {s}, e : {e}, mid : {mid}, total: {total}, t: {t}')

    if total < t:
        binary(mid+1,e,t)
    elif total == t:
        print(mid)
    else:
        binary(s,mid,t)

binary(0,maxn,M)