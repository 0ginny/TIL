'''
시작 : 21:17

0. 문제이해
 길이가 L인 문자열이 현재 편집기에 입력되어 있으면, 커서가 위치할 수 있는 곳은 L+1가지 경우가 있다.
 L	:커서를 왼쪽으로 한 칸 옮김 (커서가 문장의 맨 앞이면 무시됨)
D	:커서를 오른쪽으로 한 칸 옮김 (커서가 문장의 맨 뒤이면 무시됨)
B	:커서 왼쪽에 있는 문자를 삭제함 (커서가 문장의 맨 앞이면 무시됨)
삭제로 인해 커서는 한 칸 왼쪽으로 이동한 것처럼 나타나지만, 실제로 커서의 오른쪽에 있던 문자는 그대로임
P $	:$라는 문자를 커서 왼쪽에 추가함
 명령어가 수행되기 전에 커서는 문장의 맨 뒤에 위치

 모든 명령어를 수행하고 난 후 편집기에 입력되어 있는 문자열을 구하는 프로그램

 입력 :
 첫째 줄에는 초기에 편집기에 입력되어 있는 문자열 N < 100000
 둘째 줄에는 입력할 명령어의 개수를 나타내는 정수 M(1 ≤ M ≤ 500,000)이 주어진다
 셋째 줄부터 M개의 줄에 걸쳐 입력할 명령어

 1. 아이디어 구현
 - 문자열을 리스트로 받음.단 rstrip
 - L, D : idx 수정
 - pop(idx) N
 - P, insert N
  각각의 시간복잡도 구해보자
  
  시간초과래 N*M 안됨

  시간복잡도 문제에선 굳이 결과를 리스트에 저장하지 않고, 변수에 저장했다가 마지막에 처리하면돼.
'''

import sys

input = sys.stdin.readline

word = list(input().rstrip())

M = int(input())
l = len(word)
idx = l


def edit(commend):
    global idx, l
    if commend == 'L':
        idx -= 1

    elif commend == 'D':
        idx += 1

    # 여기부터 시간복잡도 문제가 있어.
    elif commend == 'B':
        if idx != 0:
            word.pop(idx - 1)
            l -= 1
            idx -= 1
    else:
        _, x = commend.split()
        word.insert(idx, x)
        l += 1
        idx += 1
    if idx < 0:
        idx = 0
    if idx > l:
        idx = l
    # print(idx, word)


for _ in range(M):
    commend = input().rstrip()
    edit(commend)

print(''.join(word))
