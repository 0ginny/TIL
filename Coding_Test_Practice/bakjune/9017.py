'''
시작 : 10:10
종료 : 10:40

0. 문제 이해
한 팀은 여섯 명
팀 점수는 상위 네 명의 주자의 점수를 합
이 점수를 더하여 가장 낮은 점수를 얻는 팀이 우승
여섯 명의 주자가 참가하지 못한 팀은 점수 계산에서 제외
동점의 경우에는 다섯 번째 주자가 가장 빨리 들어온 팀이 우승
여섯 명 보다 많은 선수가 참가하는 팀은 없고, 적어도 한 팀은 참가 선수가 여섯이며, 모든 선수는 끝까지 완주



입력 :
-   T 개의 테스트 케이스
- 각 테스트 케이스의 첫 번째 줄에는 하나의 정수 N (6 ≤ N ≤ 1,000)
- 두 번째 줄에는 팀 번호를 나타내는 N 개의 정수

출력 :
하나의 테스트 케이스에 대한 우승팀의 번호를 한 줄에 출력


1. 아이디어
구현
- 테스트 수 구하기 -> 모든 경우 결과를 result에 저장한 후 프린트
- 테스트 당 구현
    - 먼저 6명 이하인 팀 찾기 -> 그 후 해당 내용 제거
    - 나머지를 순서대로 1, 2, 3, 4 더하기
        - 딕셔너리 3개
            - 각 팀의 총합
            - 각 팀의 완주 인원
            - 각 팀의 5등 등수
        - 해당 딕셔너리를 비교해서 우승팀 출력

'''

import sys

input = sys.stdin.readline

T = int(input())




result = []
for _ in range(T):
    N = int(input())
    runner = list(map(int,input().split()))
    run_set = set(runner)
    # 6명 이하인 팀 찾기:
    ex = []
    for r in run_set:
        if runner.count(r) < 6 :
            ex.append(r)

    # 3개의 딕셔너리 체우기
    total_dict = {r : 0 for r in run_set if r not in ex}
    fin_dict = total_dict.copy()
    five_dict = total_dict.copy()

    score = 1
    for r in runner:
        if r not in ex:
            if fin_dict[r] < 4: # 4번째 전까진 score 합
                total_dict[r] += score
                fin_dict[r] += 1
            elif fin_dict[r] == 4: # 5번째 선수는 score 저장
                five_dict[r] = score
                fin_dict[r] += 1
            score += 1

    # print(total_dict)
    # print(five_dict)
    # 결과 비교
    minr = 4000
    winner = 0
    for r in run_set:
        if r not in ex:
            if minr > total_dict[r]:
                winner = r
                minr = total_dict[r]
            elif minr == total_dict[r]:
                if five_dict[winner] > five_dict[r]:
                    winner = r
    result.append(winner)

for ans in result:
    print(ans)