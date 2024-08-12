'''
시작 : 10:42

0.문제이해
(x,y) 모두 큰 순서대로 랭크만들기
- 입력 :
    - N
        - 사람 수
        - 2 ~ 50
    - x y
        - x 몸무게
        - y 키
        - 10 <= x,y <= 200
- 출력 :
    - N 명의 순서대로 등수
        - 등수는 자신보다 덩치가 큰 사람 +1 (일반적인 등수가 아니야)

1. 아이디어
- 둘 다 커야해
    - 결국 등수가 같아야 해당 등수고 아닌 사람들을 그 사이 등수야
- 일닽 키와 몸무게로 등수를 재 (동일한 경우는 공동 순위로 둬야해.)
    - 단순 람다 정렬로는 안돼.
        - set 으로 바꾸고 list로 다시 바꿔서 그것의 인덱스를 구하면 등수야.
    - 둘다 크다는 걸 어떻게 판별하지?
        - 2,6 등과 3,3 등이 있으면 구분이 안되잖아.
        -심지어 2,6 , 4,4 3,3 이면 3명이 동일한 순서야. 아니다
            - 덩치가 큰 사람의 수가 등수니까 등수가 1,2,3 동일 할 필요는 없어.
        - weight 랭크와 height 랭크 중 더 작은 수가 등수야. 아니 이것도 아니야
            - 1,1 , 2,7 , 3,6 , 5,5, , 4,4 라면?
                - 1,1 1등 4,4 는  2등, 나머지 3등이 돼.
        - 그럼 일일히 비교해야지.
            - 일단 people 에서 weight 등수를 재.
                - 그리고 그 앞 weight 를 가진 사람을 모두 추출해
                (이 전에 미리 rank : [해당 ] 라는 딕셔너리를 만들어놔, 그 후

                    - 그 사람들과 height를 비교해서 자신보다 큰 사람이 있으면 등수를 + 해



'''

import sys

input = sys.stdin.readline

N = int(input())
weights = []
heights=[]
people = []
for _ in range(N):
    w, h = map(int,input().split())
    weights.append(w)
    heights.append(h)
    people.append((w,h))

weights.sort(reverse=True)
heights.sort(reverse=True)


# print(weights)
# print(heights)

weights_dict = {}
heights_dict = {}

for i in range(N):
    if i == 0:
        weights_dict[weights[i]] = i+1
        heights_dict[heights[i]] = i+1
        continue
    if weights[i-1] == weights[i] :
        weights_dict[weights[i]] = weights_dict[weights[i-1]]
    else :
        weights_dict[weights[i]] = weights_dict[weights[i-1]] + 1

    if heights[i] == heights[i-1]:
        heights_dict[heights[i]] = heights_dict[heights[i-1]]
    else:
        heights_dict[heights[i]] = heights_dict[heights[i-1]] +1

# print(weights_dict)
# print(heights_dict)

ranks = {}
weight_rank = {rank : [] for rank in weights_dict.values()}
for i in range(N):
    w,h = people[i]
    weight_rank[weights_dict[w]].append(people[i])

# print(weight_rank)

for i in range(N):
    w, h = people[i]
    cnt = 1
    for j in range(1,weights_dict[w]):
        for  _, nh in weight_rank[j]:
            if nh > h :
                cnt += 1
    print(cnt,end=' ')
