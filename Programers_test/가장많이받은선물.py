"""
0. 문제이해
    - 입력 : 사람 이름들, ' '로 split 할 선물'
    - 출력 : 가장 많이 받는 선물 '수'
    - 선물 받는 조건 :
        - 1대1로 선물 준 게 더 많을 경우,
        - 같다면 자신이 선물지수가 그 상대보다 높을 경우
            - 선물지수 : 준선물 - 받은 선물
1. 문제 풀이
- fd : 사람 딕셔너리, key index, value 이름
- fgd : 선물지수 딕셔너리, key index, value 선물지수
- fl : 2차원 리스트 [s][e] : s = 주는 사람, e = 받는사람
- ansd : 사람 선물받을 딕셔너리 , key 이름, value 받는 선물수
- fl[i][j] >fl[j][i] 인 경우
    - ansd[i] += 1
- == 경우
    fd[i] > fd[j] 인 경우 ansd[i] += 1
- 반대는 반대로
- 출력 max(ansd.values)
"""


def solution(friends, gifts):
    answer = 0
    fd = {}
    fgd = {}

    l = len(friends)
    for i, name in enumerate(friends):
        fd[name] = i
        fgd[i] = 0

    ans = [0] * l
    fl = [[0] * l for _ in range(l)]

    for gift in gifts:
        giver, receiver = gift.split()
        fgd[fd[giver]] += 1
        fgd[fd[receiver]] -= 1
        fl[fd[giver]][fd[receiver]] += 1

    for i in range(l):
        for j in range(i + 1, l):
            # print(f' i : {i}, j :: {j}' )
            if fl[i][j] > fl[j][i]:
                ans[i] += 1
            elif fl[i][j] < fl[j][i]:
                ans[j] += 1
            else:
                if fgd[i] > fgd[j]:
                    ans[i] += 1
                elif fgd[i] < fgd[j]:
                    ans[j] += 1

    # print(f'nl : \n{fl}\n fgd : \n{fgd}\n ans : \n{ans}')

    return max(ans)