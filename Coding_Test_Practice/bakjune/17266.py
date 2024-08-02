'''
시작 : 10:50
정지 : 11:17
재시작 : 11:55

0.  문제 이해
 가로등을 설치할 개수 M과 각 가로등의 위치 x들의 결정
 가로등은 높이만큼 주위를 비출 수 있다.
  최소한의 높이로 굴다리 모든 길 0~N을 밝히고자 한다.
  단 가로등은 모두 높이가 같아야 하고, 정수
가로등의 높이가 H라면 왼쪽으로 H, 오른쪽으로 H만큼 주위를 비춘다

입력
- 첫 번째 줄에 굴다리의 길이 N 이 주어진다. (1 ≤ N ≤ 100,000)
    - 주의할 사항느 0 ~ N 까지를 채워야해
- 두 번째 줄에 가로등의 개수 M 이 주어진다. (1 ≤ M ≤ N)
-  M 개의 설치할 수 있는 가로등의 위치 x 가 주어진다. (0 ≤ x ≤ N)
- 가로등의 위치 x는 오름차순으로 입력받으며 가로등의 위치는 중복되지 않으며, 정수

출력
- 굴다리의 길이 N을 모두 비추기 위한 가로등의 최소 높이

1. 아이디어
구현
- N+1 길이의 chk 리스트 생성
- 가로등 위치 리스트 채우기
- for p in position:
    - 앞쪽부터 chk 리스트를 채우고 만약 chk list가 False 가 생기게 되면 continue
    - continue 전에 h += 1
    - 리스트를 모두 True로 만드는 최소 h 구하기

--- chk를 채우는 형식으로 하니 시간초과가 일어나
단순 숫자 연산으로 가야해.

반례 :
7
2
0 5
answer : 3
'''

import sys

input = sys.stdin.readline

N = int(input())
M = int(input())
position = list(map(int, input().split()))
# print(position)

# 한번 틀렸어
# 모든 경우의 수를 다 포용하는지 살펴봐
for h in range(1, 50000):  # 높이 1 ~ 50000 까지 해야 100000 N 개의 굴다리 모두 수용가능
    chk = [False] * (N + 1)  # 굴다리는 0 ~ N 까지야
    fin = False  # 해당 h 에서 이미 전체가 True가 됨
    for p in position:  # 모든 포지션 선택
        minl = max(0, p - h)  # True 로 채울 시작위치
        ## 이 부분에서 틀린 거였어. 불이 켜지는 건 p+h-1 까지 켜져야 그 사이 빈 공간이 없는거야
        if p == position[-1]: # 마지막 가로등은 채우는게 맞네
            maxl = min(N + 1, p + h + 1)  # False로 채울 끝 위치
        else:
            maxl = min(N + 1, p + h)  # False로 채울 끝 위치
        # print(f'{p} 에서 높이 {h}')
        for i in range(minl, maxl):  # 해당 가로등 범위 전부 True 전환
            chk[i] = True
        # print(chk)

        # 슬라이싱으로 체크한 경우 시간초과
        # 만약 켜진 가로등 이전에 False가 있는 경우 position 종료 h 리뉴얼
        if minl != 0:
            if chk[minl - 1] == False or chk[0] == False:
                break
        # 현재 상황은 maxl 이전은 모두 True 인 경우야
        # 마지막 칸이 True 인 경우 모두가 켜진 경우야
        if chk[-1] == True:
            fin = True
            break
    if fin == True:
        break
print(h)
