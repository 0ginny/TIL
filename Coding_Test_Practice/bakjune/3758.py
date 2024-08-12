''''
시작 : 10:27
종료 : 10:54

0. 문제 이해
한 문제에 대한 풀이를 여러 번 제출할 수 있는데, 그 중 최고 점수가 그 문제에 대한 최종 점수가 된다.
(만약 어떤 문제에 대해 풀이를 한번도 제출하지 않았으면 그 문제에 대한 최종 점수는 0점이다.)
순위는 (당신 팀보다 높은 점수를 받은 팀의 수)+1 이다.

점수가 같으면
    최종 점수가 같은 경우, 풀이를 제출한 횟수가 적은 팀의 순위가 높다.
    최종 점수도 같고 제출 횟수도 같은 경우, 마지막 제출 시간이 더 빠른 팀의 순위가 높다.

- 입력 :
    T : 테스트 수
    n, k, t, m : 팀수, 문제 수, 우리팀, 로그엔트리 수
        k ≤ 100, 1 ≤ t ≤ n, 3 ≤ m ≤ 10,000
    i, j ,s : 팀id, 문제번호, 획득 점수
        1 ≤ i ≤ n, 1 ≤ j ≤ k, 0 ≤ s ≤ 100


1. 아이디어
- 구현
    - 최종 점수 구하기
        - 문제 수 만큼 0 점으로 하는 [0] * j + 1를 값으로 갖는 딕셔너리 생성
        - 아래로 내려가면서, max(dict[id][problem],ans) 로 리뉴얼
        - 최종에 팀별 총합 계산후 비교
    - 최종 점수 같으면, 풀이 적게한 팀 우위
        각 팀별 풀이한 횟수 체크
    - 풀이 수도 같으면 빨리 제출한 팀이 우위
        각 팀별 최종 제출 순위 체크
마지막, 우리팀보다 최종점수가 높거나 풀이 적게하고, 빨리 제출한 팀이 몇팀인지 + 1
'''

import sys

input = sys.stdin.readline

T = int(input())

ans = []
for _ in range(T):
    n, k, t, m = map(int,input().split())

    # 점수를 저장할 딕셔너리
    sdict = { n : [0] * (k+1) for n in range(1,n+1)}
    # 제출 개수를 저장할 딕셔너리
    ndict = { n : 0 for n in range(1,n+1)}
    # 최종 제출 로그를 저장할 딕셔너리
    ldict = { n : 0 for n in range(1,n+1)}
    for l in range(m):
        i, j, s = map(int,input().split())
        # 제출한 점수 중 최대
        sdict[i][j] = max(sdict[i][j],s)
        ndict[i] += 1
        ldict[i] = l
    # 최종 점수
    cnt = 1
    base = sum(sdict[t])
    for a in range(1,n+1):
        if a != t:
            sums = sum(sdict[a])
            if sums > base:
                cnt += 1
            elif sums == base:
                # 풀이한 수 가 적으면
                if ndict[a] < ndict[t]:
                    cnt += 1
                elif ndict[a] == ndict[t]:
                    # 마지막 제출이 더 작으면
                    if ldict[a] < ldict[t] :
                        cnt+= 1
    ans.append(cnt)
for pp in ans:
    print(pp)