'''
시작 : 12 :11
종료 : 12:32
문제 이해
세 종류의 문자로 이루어져 있으며 양쪽 모두 'D', 'G', 'O' 가 하나씩 있으므로 이 둘은 같은 구성을 갖는다.
두 단어가 같은 구성을 갖는 경우, 또는 한 단어에서 한 문자를 더하거나, 빼거나, 하나의 문자를 다른 문자로 바꾸어 나머지 한 단어와 같은 구성을 갖게 되는 경우에 이들 두 단어를 서로 비슷한 단어
입력으로 여러 개의 서로 다른 단어가 주어질 때, 첫 번째 단어와 비슷한 단어가 모두 몇 개인지 찾아 출력하는 프로그램을 작성하시오.

- 입력
N : 입력 수  100 이하
단어들 : 길이 10 이하

- 출력 : 첫단어와 비슷한 단어 수

1. 아이디어
구현 :
- 일단 비슷할 케이스가 3개야
    - 글자수가 1개 적을 경우
        - 해당 단어의 모든 원소가 기준 단어에 있어야해
            - 해당 단어를 for문하고 하나씩 remove 해보고 1개 남으면?
                - 시간복잡도는? L * N
    - 글자수가 같을 경우
        - 모든 원소가 같을 경우
            이것도 remove 로
        - 단 하나만 다를 경우
            남은게 단 하나나    - 글자수가 1개 많을 경우
        - 기존 단어의 모든 원소가 해당 단어에 있을 경우
'''

import sys

input = sys.stdin.readline

N = int(input())
cnt = 0



base = []

def chk(w):
    # 길이가 우선 1 이하로 차이나야해
    l = len(w)
    bl = len(base)
    test= base.copy()
    if bl-l == 1 or l-bl == 0:
        for i in w:
            try :
                test.remove(i)
            except : pass
        if len(test) <= 1:
            return True
    elif l- bl == 1 :
        for j in test:
            try:
                w.remove(j)
            except:
                pass
        if len(w) == 1:
            return True
    return False


for i in range(N):
    word = list(input().rstrip())
    if i == 0 :
        base = word
    else :
        if chk(word) :
            cnt += 1

print(cnt)