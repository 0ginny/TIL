'''
시작 : 12:11
종료 : 12:30

총 걸린 시간 : 19분

0. 입출력
- 입력 :
    N K
    - N : 1~1000 참가 국가 수
    - K : 1 ~ N 내가 순위 알기 원하는 국가
    idx g s c
    - idx : 국가 index
    - g s c : 금 은 동 수 / g+s+v 의 합은 e6 이하
- 출력 :
    K index 국가는 몇등인가?

1. 아이디어
구현 :
    - { idx : [g, s, c] } 로 저장
    - dict.values lambda sort 로 g,s,c 로 정렬
    - list.index(dict[idx])로 순위 찾기
2. 시간복잡도
- 1000 개 국가 sort
    1000log1000

'''

import sys

input = sys.stdin.readline

N, K = map(int, input().split())
lands = {}
for _ in range(N):
    idx, g, s, c = map(int,input().split())
    lands[idx] = [g,s,c]

medals = list(lands.values())
# print(medals)
medals.sort(key=lambda x: (-x[0],-x[1],-x[2]))
# print(medals)
print(medals.index(lands[K])+1)