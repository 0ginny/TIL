"""
시작 3:26
0. 문제 이해
- T 번의 테스트 실행
- 자연수 K 를 입력받아 삼각수의 덧셈으로만 표현
- 최소 삼각수를 3번 더했으면 1 그 이하라면 0 출력

1. 아이디어
- 일단 삼각수 리스트 부터 만들어야겠지?? n(n+1)/2
    - 몇 번째부터 K를 넘는 n 을 찾기 (최대 n 은 45 ~ 46)
    - 그 만큼을 tri 리스트에 넣기
- 그냥 전체를 구할까??
    - 시간 복잡도 50 ^ 3 = 125000 가능 , Test 수는 상관 없나봄.
    - 재귀
        넘지 않는 선에서 전부 돌리기
        값이 같아진 경우 몇번째 재귀인지 확인하기
            - 3번째면 ans = 1
"""
import sys
input = sys.stdin.readline

T = int(input())

tri = []

def tri_list(n): # 모든 삼각수 리스트
    global tri
    for i in range(1,n):
        n_tri = i * (i + 1) / 2
        # print('n_try : ',n_tri)
        if n_tri > n:
            break
        tri.append(n_tri)

chk = 0

def rec(num,target,depth):
    global chk, tri
    # 종료 조건
    if num == target:
        if depth == 3:
            chk = 1
            # print("성공")
        return
    if depth >= 3 :
        return
    #재귀
    for tn in tri:
        new_n = num + tn
        rec(new_n,target,depth+1)


result = []
for i in range(T):
    # print(f'{i} 번째 테스트 \n')
    tri = []
    chk = 0
    N = int(input())
    tri_list(N)
    rec(0,N,0)
    result.append(chk)

for c in result:
    print(c)
