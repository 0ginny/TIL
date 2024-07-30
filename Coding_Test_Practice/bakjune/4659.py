'''
시작 : 12 :00
종료 : 12:21

0. 문제이해
- 모음은 (a,e,i,o,u)
- 모음 3번 연속 혹은 자음 3번 연속이면 안됨
- ee, 와 oo 를 제외한 같은 글자 연속이면 안됨

- 입력 :
    - 각 단어
        - 맞는지 확인
    - end
        - 종료
- 출력 :
    - <단어> is acceptable.
    - <단어> is not acceptable.

1. 아이디어
- 구현
    - 조건에 맞는지 안맞는지 함수 생성
    - 입력받으면 함수 확인
    - 결과 출력
'''

import sys

input = sys.stdin.readline

mo = list('aeiou')

def check(word) -> bool:
    last = ''
    # 모음이 반드시 하나 이상
    one = False
    for m in mo:
        if m in word:
            one = True
            break
    if one == False:
        return False

    # 자음 모음 3번 연속 안됨
    cnt = 0
    is_mo = False
    for s in word:
        if s in mo:
            if is_mo == False:
                is_mo = True
                cnt = 1
            else :
                cnt += 1
        else : # 자음일 경우
            if is_mo == True:
                cnt = 1
                is_mo =False
            else: # 이전 자음
                cnt += 1
        if cnt >= 3 :
            return False

        # 같은 글자가 연속으로 2번 온다면
        if s == last:
            if s not in ['e','o']: # 심지어 e, o 도 아니라면
                return False
        else :
            last = s
    # 모든 조건을 통과 했을 때
    return True

words = []
while 1 :
    word = input().rstrip()
    if word == 'end':
        break

    words.append(word)

for word in words:
    if check(word):
        print(f'<{word}> is acceptable.')
    else :
        print(f'<{word}> is not acceptable.')