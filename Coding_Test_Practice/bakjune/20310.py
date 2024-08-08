'''
시작 : 10:57

0. 문제이해
0과 1로 이루어진 문자열
$S$를 보았다.
$S$가 포함하는 0의 개수와
$S$가 포함하는 1의 개수는 모두 짝수

문자 중 절반의 0과 절반의 1을 제거하여 새로운 문자열
$S'$를 만들고자 한다

$S'$로 가능한 문자열 중 사전순으로 가장 빠른 것

입력 : 문자열 S
출력 S'로 사전순으로 가장 빠른 것 (000001111) 이겠지?

1. 아이디어
어차피 전부 짝수면 너무 쉬운 거 아니야?
- S 의 0의 갯수 새 z
- S 의 1의 갯수 새 o
0 * z/2 + 1 * o/ 2

아니다
만약 00100100 이면
0010 이 되야해.

그럼 그리디로 0은 맨 뒤부터 없애고
1은 맨 앞부터 없애면 되겠다.


'''

import sys

input = sys.stdin.readline

S = list(str(input().rstrip()))
o = S.count('1')
l =len(S)
z = l - o

o /= 2
z /= 2

ocnt = 0
zcnt = 0

ans= ''
for s in S:
    if s == '0':
        if zcnt < z:
            ans += s
            zcnt += 1
    else :
        if ocnt < o :
            ocnt += 1
        else :
            ans += s
print(ans)