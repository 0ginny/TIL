'''
시작 : 10: 53
종료 : 11: 21

0. 문제 이해
우주선은 위에서 아래로 내려가
각 왼쪽 중앙 오른쪽으로 내려갈 수 있어
단, 이전 방향과 중복되면 안돼
각 숫자는 우주선이 지날때 드는 연료량
최소 연료를 구해라.
맨 처음은 아무곳에서 시작

- 입력 :
행렬 크기 N, M 행, 열
N,M 은 1 <=  <=6
원소값

1. 아이디어
그리디
어차피 뒤로 갈 수 없으니, 앞에서 최선을 구하면 돼.

대신 두 단계씩 이동해야해.

1-> 2,3
2-> 1,3
3-> 1,2

마지막은?

근데 사실 행렬이 작아서 dfs, bfs 로 푸는게 더 편할 듯.
시간복잡도 2* N * H 가능

'''

import sys

input = sys.stdin.readline

N, M = map(int,input().split())

space = [list(map(int,input().split())) for _ in range(N)]

minl = 6 * 100

dj = [-1,0,1]
stack = []

def bfs(i,j,d,temp):
    if i == N -1 :
        global minl
        minl = min(minl,temp)
        return
    ni = i + 1
    for k in range(3):
        if k != d : # 이전과 중복 x
            nj = j + dj[k]

            if 0 <= nj < M:
                new_temp = temp + space[ni][nj]
                bfs(ni,nj,k,new_temp)

for j,l in enumerate(space[0]):
    bfs(0,j,-1,l)

print(minl)
