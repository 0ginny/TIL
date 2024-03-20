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
            - 실패
    - 투포인터?
        - 일단 ls 오름차순 정렬
        - left 맨 왼, right 맨 오른
            - left가 올라가면서 sum >= m 인지 확인
                - sum == m 이면 cnt += 1
                - left 고정 right 내려가면서 sum <= 인지 확인
                    - 작아졌으면 다시 left 올라가며 반복
            - left = right 되면 종료

            - 시간복잡도 : NlogN  + N  = NlogN 100000까지 가능
"""
import sys

input = sys.stdin.readline

N = int(input())
M = int(input())
ls = list(map(int,input().split()))
ls.sort()

cnt = 0
left = 0
right = N-1
while (left != right):
    if (ls[left] + ls[right]) <= M:
        if (ls[left] + ls[right]) == M:
            cnt += 1
        left += 1
    else: #(ls[left] + ls[right]) > M:
        right -= 1
print(cnt)