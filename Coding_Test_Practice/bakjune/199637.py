'''
시작 : 9:56

0. 문제이해
전투력 10,000 이하의 캐릭터는 WEAK, 10,000 초과 그리고 100,000 이하의 캐릭터는 NORMAL, 100,000 초과 그리고 1,000,000 이하의 캐릭터는 STRONG 칭호를 붙여준다

입력 :
첫 번째 줄에는 칭호의 개수 N (1 ≤ N ≤ 105)과 칭호를 출력해야 하는 캐릭터들의 개수 M (1 ≤ M ≤ 105)이 빈칸을 사이에 두고 주어진다. (1 ≤ N, M ≤ 105)
칭호는 전투력 상한값의 비내림차순으로 주어진다.


출력 :

출력할 수 있는 칭호가 여러 개인 경우 가장 먼저 입력된 칭호 하나만 출력한다.
'''

import sys

input = sys.stdin.readline

N, case = map(int, input().split())

label_dict = {}
for _ in range(N):
    label, score = input().rstrip().split()
    score = int(score)
    try :
        if label_dict[score] != None:
            pass
    except KeyError:
        label_dict[score] = label

def chk(n) -> str:
    for (s, l) in label_dict.items():
        if n <= s:
            return l
    return "불가능한 값"

ans = []
for _ in range(case):
    num = int(input())
    ans.append(chk(num))

for a in ans:
    print(a)