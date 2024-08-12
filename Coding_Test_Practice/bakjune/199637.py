'''
시작 : 9:56

0. 문제이해
전투력 10,000 이하의 캐릭터는 WEAK, 10,000 초과 그리고 100,000 이하의 캐릭터는 NORMAL, 100,000 초과 그리고 1,000,000 이하의 캐릭터는 STRONG 칭호를 붙여준다

입력 :
첫 번째 줄에는 칭호의 개수 N (1 ≤ N ≤ 10^5)과 칭호를 출력해야 하는 캐릭터들의 개수 M (1 ≤ M ≤ 10^5)이 빈칸을 사이에 두고 주어진다. (1 ≤ N, M ≤ 105)
칭호는 전투력 상한값의 비내림차순으로 주어진다.
해당하는 칭호가 없는 전투력은 입력으로 주어지지 않는다.
    - 일단 전투력의 다른 제약조건은 없어. 중복은 가능한가봐, sort도 안되있을 거고

출력 :

출력할 수 있는 칭호가 여러 개인 경우 가장 먼저 입력된 칭호 하나만 출력한다.
칭호는 비 내림 차순이야.
score 가 같으면 먼저 나온 거
100 a
101 b
102 c

101 이면 b 잖아.


1. 아이디어
구현 :
    for 문 if 문
시간복잡도 실패 10 ^10

--------------
모두 list 에 넣고 sort : 10^5 * ln10^5
sort 를 하더라도 이전 순서대로 출력을 해야해.
그후 idx +=  1 하면서 비교 : 10^5
가능
---------------
runtime error index
index문제면 list가 문제야
case의 문제인가봐


'''

import sys

input = sys.stdin.readline

N, M = map(int, input().split())

label_dict = {}
for _ in range(N): #10^5
    label, score = input().rstrip().split()
    score = int(score)
    try :
        if label_dict[score] != None:
            pass
    except KeyError:
        label_dict[score] = label

raw_case = [int(input()) for _ in range(M)] # 인덱스 문제 있을 수 없음
# sort 전 index 저장

case = sorted(raw_case) # index 문제 없음

ans = {}
cnt = 0
for (s,l) in label_dict.items():
    try :
        while case[cnt] <= s: # cnt 가 없는 값일 수 있나? 그치 while break 후 for 문이 계속 진행되면
            ans[case[cnt]] = l
            cnt+=1
    except IndexError:
        break

for c in raw_case:
    print(ans[c])

# runtime error(index)