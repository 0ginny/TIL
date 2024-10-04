'''
01:18

문자열의 뒤에 A를 추가한다.
문자열의 뒤에 B를 추가하고 문자열을 뒤집는다.

이렇게 해서 S 를 T 로 바꿀 수 있으면 1 없으면 0

1. 아이디어
- 부르트포스 ? 글자수가 같아질 때까지만 반복, 그래서 바뀌는지만 확인
    시간복잡도 : 2^50 1000^5 불가능

A
BA, AA
BAB, BAA, AAA
BBAB, BAAB, AAAA,BAAA

'''
import sys

input = sys.stdin.readline


S = input().rstrip()
T = input().rstrip()
ls= len(S)
chk = 0
def dfs(T):
    global chk
    if not chk :
        if len(T) == ls :
            if S == T :
                chk = 1
                return
            return
        if T[-1] == 'A':
            dfs(T[:-1])
        if T[0] == 'B' :
            dfs(T[1:][::-1])

dfs(T)
print(chk)