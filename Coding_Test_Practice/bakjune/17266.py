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

---단순 숫자도 시간초과야
for 문을 1번만 써야해
그 후 모든 pos[n] - pos[n-1] 을 구해
그 중 가장 큰 거의 //2 +1 을 선택해
    만약 p[0]-h = 0 인 h 보다 큰지 확인
    N-p[-1] <= h 인지 확인


반례 :
7
2
0 5
answer : 3
4
2
0 4
answer : 2
'''

import sys

input = sys.stdin.readline

N = int(input())
M = int(input())
pos = list(map(int, input().split()))
# print(position)
dist = set()
for n in range(1,M):
    diff = pos[n] - pos[n-1]
    temp = diff//2 +1  if diff % 2 else diff//2
    dist.add(temp)

if dist :
    maxh = max(dist)
else : maxh = 0
h = max(pos[0],maxh,N-pos[-1])
print(h)

