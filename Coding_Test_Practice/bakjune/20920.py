'''
시작 : 10:27
종료 : 11:00

0. 문제 이해

- 조건
자주 나오는 단어일수록 앞에 배치한다.
해당 단어의 길이가 길수록 앞에 배치한다.
알파벳 사전 순으로 앞에 있는 단어일수록 앞에 배치한다
길이가 M이상인 단어들만

- 입력
첫째 줄에 단어의 개수 N과 외울 단어의 길이 기준이 되는 M
다음부터 외울 단어 입력 (단어길이 <= 10)

- 출력
단어장 출력

1. 아이디어
구현
- 만약 len(word) < M 이면 스킵

- 자주 나오는 단어 구현
    - dict 에 단어별 출현 횟수 저장 (N)
    - 각 value가 같은 것들끼리 list 저장 (N)
    - list끼리 알파벳 정리 (root(N)* root(N)lnroot(N) -- 가능할 거 같은데?)
    - 해당 리스트 전부 더하기

'''

import sys

input = sys.stdin.readline

N, M = map(int,input().split())
wlist = [ input().rstrip() for _ in range(N)]

# 해당 단어들 dict에 저장
wdict = {}
for w in wlist:
    if len(w) >= M:
        try :
            wdict[w] += 1
        except :
            wdict[w] = 1

word_list = list(wdict.keys())
word_list.sort(key= lambda x : (-wdict[x],-len(x),x))

for word in word_list:
    print(word)

