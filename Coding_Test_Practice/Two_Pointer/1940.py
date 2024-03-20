"""
시작 1:07
0. 문제이해
    - 입력 : 재료수 ( 리스트 크기 ) N, 목표값 M, L 리스트
    - 출력 : 두 L의 합 == 목표값인 수
    - 숫자 범위 :
        - 고유번호 합 M : e7 ( 목표값
        - 잴료 수 :  N : 15000
        - 고유번호 : L : e5

1. 아이디어
    - ls에 모든 고유번호 저장
    - 이중 for 문으로 모두 검색
        - 시간복잡도 N*(N-1) 225000000
        - 아주 조금 넘길 거 같은데?
            - 대신 숫자를 찾으면 거기서 멈추면 가능하지 않을까?

"""
import sys

input = sys.stdin.readline

N = int(input())
M = int(input())
ls = list(map(int,input().split()))

cnt = 0
for i in range(N-1):
    for j in range(i,N):
        if ls[i] + ls[j] == M :
            cnt += 1
print(cnt)

# 시간초과 실패