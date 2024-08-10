'''
시작 : 13:00
종료 : 13:31

0. 문제이해
플레이어가 입장을 신청하였을 때
    매칭이 가능한 방이 없다면 새로운 방을 생성하고 입장시킨다.
        이떄 해당 방에는 처음 입장한 플레이어의 레벨을 기준으로 -10부터 +10까지 입장 가능하다.
입장 가능한 방이 있다면 입장시킨 후 방의 정원이 모두 찰 때까지 대기시킨다.
이때 입장이 가능한 방이 여러 개라면 먼저 생성된 방에 입장한다.
방의 정원이 모두 차면 게임을 시작시킨다.


입력 :

첫 번째 줄에는 플레이어의 수 p(1 ≤ p ≤ 300)와 방의 정원 m(1 ≤ m ≤ 300)가 주어진다.
두 번째 줄부터 p개의 줄에는 플레이어의 레벨 l (1 ≤ l ≤ 500)과 닉네임 n이 공백을 두고 주어진다.
입력된 순서대로 게임을 시작한다.
닉네임은 중복되지 않으며 공백을 포함하지 않는 알파벳 소문자로 되어있으며 닉네임의 길이는 16을 넘지 않는다.

출력 :
 게임의 시작 유무와 방에 들어있는 플레이어들의 레벨과 아이디를 출력
방은 생성된 순서대로 출력
방에 있는 플레이어들의 정보는 닉네임이 사전순으로 앞서는 플레이어부터 출력한다.
방이 시작되었으면 Started!를 대기 중이면 Waiting!을 출력시킨다

1. 아이디어
- 구현 :
    맨 처음 최대 길이 설정
        dict[그룹인덱스] = {'num' : int, 'max' : int , 'min', int, 'people' : list([level,alpha)}
    들어갈 수 있는 그룹이 있는지는 어떻게 찾지??
        for 문으로 모든 그룹을 확인? 300 * 300 가능하긴 해
            인원수가 T가 넘지 않는 곳
            해당 레벨이 상한 하한에 적합한 곳
        전부 확인했는데 없다?
            딕셔너리 새로 생성
    모든 경우 다 돌고
        모든 people list sort 300 * log300 가능
        그리고 결과 출력

'''

import sys

input = sys.stdin.readline

N, M = map(int, input().split())

idx = 0
ans_dict = {}
for i in range(N):
    level, name = input().rstrip().split()
    level = int(level)
    if i == 0:
        ans_dict[idx] = {'num': 1,
                         'max': level + 10,
                         'min': level - 10,
                         'people': [[level, name]]}
    else :
        add_chk = False
        for j in range(0,idx+1):
            # 그룹 안에 들어갈 수 있는지 확인
            # 먼저 상한 하한 맞는지 확인
            if ans_dict[j]['min'] <= level <= ans_dict[j]['max']:
                # 만약 num 이 상한을 넘지 않았을 경우
                if ans_dict[j]['num'] < M :
                    ans_dict[j]['people'].append([level,name])
                    ans_dict[j]['num'] += 1
                    add_chk = True
                    break

        # 만약 추가되지 않았다면
        if add_chk == False:
            idx += 1
            ans_dict[idx] = {'num': 1,
                             'max': level + 10,
                             'min': level - 10,
                             'people': [[level, name]]}

# 출력
for d in ans_dict.values():
    if d['num'] == M :
        print('Started!')
    else :
        print('Waiting!')

    people = d['people']
    people.sort(key = lambda x : x[1])
    for p in people:
        print(f'{p[0]} {p[1]}')

