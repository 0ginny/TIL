"""
시작 : 9:27
0 문제 이해
- 기울어서 빼야해, 한번에 끝까지 가는 거지
- 항상 테두리는 #으로 막혀있어
- 파랑이 나오면 탈락
- 입력 : 행, 열
    맵 :
         '.', '#', 'O', 'R', 'B' 로 이루어져 있다.
         '.'은 빈 칸을 의미하고,
         '#'은 공이 이동할 수 없는 장애물 또는 벽을 의미하며,
         'O'는 구멍의 위치를 의미한다. 'R'은 빨간 구슬의 위치,
         'B'는 파란 구슬의 위치이다.
- 출력 : 최소 성공 횟수
- 숫자 범위 3< n,m < 10

1. 아이디어
- 최소 횟수이므로 dfs가 적격
- 탈락의 경우 : b == o 인 경우
- 10번이 최대 움직일 수 있는 경우

- dfs 로 4 방향씩 10번 돌려
    - 파란색이 나오면 바로 break,
    - 빨간색이 나오면 break 후 값 저장, ans
    - 최종 ans 중 최솟값 출력
- 주의사항 :
    - 돌릴 때 구슬이 모두 이동하지만, 빨간색과 파란색이 곂칠 경우 초기 값을 이용해서 위치를 결정해주자.
"""
import sys
from collections import deque

input = sys.stdin.readline

H , W = map(int,input().split())
bd = [list(input().rstrip()) for _ in range(H)]

# 초기 위치 찾기
for i in range(H):
    for j in range(W):
        if bd[i][j] == 'B' :
            bi,bj = i,j
        elif bd[i][j] == 'R':
            ri, rj = i, j

di = [0,1,0,-1]
dj = [1,0,-1,0]

ans = []
visit = deque()
visit.append((ri,rj,bi,bj))

def rec(n,ri,rj,bi,bj):
    if n == 11 : return # 10번 초과로 돌렸다면 종료

    for k in range(4): # 굴리는 방향 4번
        bgoal = False
        nri, nrj, nbi, nbj = ri, rj, bi, bj
        # 중복일 경우 찾기 위해 움직인 횟수 변수 생성
        cntr= 0
        cntb= 0

        while bd[nbi][nbj] != '#' : # 파란공부터 굴리기
            nbi += di[k]
            nbj += dj[k]
            cntb+=1
            # 파란 공 나온 경우 (빨공보다 먼저)
            if bd[nbi][nbj] == 'O':
                bgoal = True
                # print(f' 파랑골 # nri : {nri} , nrj : {nrj} , nbi : {nbi}, nbj : {nbj} , n : {n}')
                break
        if bgoal : continue # 파랑골일 경우 넘기기

        while bd[nri][nrj] != '#': # 빨간공 굴리기
            nri += di[k]
            nrj += dj[k]
            cntr+=1
            # 빨간 공 나온 경우
            if bd[nri][nrj] == 'O':
                ans.append(n)
                # print(f' 빨강골 # nri : {nri} , nrj : {nrj} , nbi : {nbi}, nbj : {nbj} , n : {n}')
                # print(ans)
                break

        # 둘 다 '#' 에 있는 경우
        if bd[nbi][nbj] == '#' and bd[nri][nrj] == '#' :
            # 둘이 같은 위치일 경우
            if nbi == nri and nbj == nrj:
                if cntr > cntb:
                    nri -= di[k]
                    nrj -= dj[k]
                else :
                    nbi -= di[k]
                    nbj -= dj[k]
            # 다음 단계로 # 이전 자리로 초기화
            nri -= di[k]
            nrj -= dj[k]
            nbi -= di[k]
            nbj -= dj[k]
            if (nri, nrj, nbi, nbj) not in visit: # 지나지 않은 경우만 다음 단계로.
                # print(f' 모두 # nri : {nri} , nrj : {nrj} , nbi : {nbi}, nbj : {nbj} , K : {k}, n : {n}, ' )
                visit.append((nri, nrj, nbi, nbj)) # 지난 위치 넣기
                rec(n+1, nri, nrj, nbi, nbj)
                visit.remove((nri, nrj, nbi, nbj)) # 이미 다 돌았으면 위치 빼기

rec(1,ri,rj,bi,bj)

if ans :
    print(min(ans))
else : print(-1)

''' feedback
1. visit을 제대로 구하지 못했어. bfs, dfs 에서 visit은 항상 생각하자.
2. while 을 여러번 써도 시간복잡도는 비슷해. 그러니까 햇갈리지 않게 여러번 쓰자. 
3. 재귀의 경우 재귀 돈 후에 초기화(visit, q)를 해줘야해.
4. 복사를 너무 남용하지 말자. 오히려 단순한 오타가 더 찾기 어려워. 차라리 단축없이 내가 그냥 작성해. 디버깅 하는 것보다 쉬워.
5. 일단 예시는 다 돌아갔는데 문제가 생겼다? 그러면 오타있는지부터 찾아. 
6. 그리고 문제 조건 빠뜨리진 않았는지 다시 찾아.
'''
