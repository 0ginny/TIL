'''
시작 : 10:09
종료 : 10:32

0. 문제이해
- 와 * 로 이루어진 쿠키 도면으로
심장의 위치 좌표와 팔다리를 구분해라

- 입력 :
    N : NxN 크기 도면
- 출력 :
    x,y : 심장좌표
    la, ra, w, ll,rl : 왼팔, 오른팔, 허리, 왼다리, 오른다리 길이

1. 아이디어
구현
- 맵을 좌표로 찍어
- 우선 심장을 찾아. 좌우, 위아래 * 이 있는 유일한 형태
- 심장기준 왼쪽, 오른쪽, 아래로 몇칸씩 * 이 있는지 찾아
- 허리 아래 기준 대각선 왼쪽, 오른쪽이 아래로 몇칸 * 있는지 찾아
'''

import sys

input = sys.stdin.readline

N = int(input())
plate = [list(input().rstrip()) for _ in range(N)]


# 심장찾기
def find_heart():
    for y in range(N):
        for x in range(N):
            if plate[y][x] == '*':
                # 위에서부터 내려오므로
                # 반드시 맨처음 *는 머리야.
                # 머리 바로 밑이 심장
                return y+1, x

def cnt_body(y,x, dx, dy):
    cnt = 0
    while 1 :
        y += dy
        x += dx
        if 0 <= x < N and 0 <= y < N:
            if plate[y][x] == '*':
                cnt += 1
                continue
        break
    return cnt

y,x = find_heart()
la = cnt_body(y,x,-1,0)
ra = cnt_body(y,x,1,0)
w = cnt_body(y,x,0,1)
rl = cnt_body(y+w,x-1,0,1)
ll = cnt_body(y+w,x+1,0,1)

print(y+1,end=' ')
print(x+1)
print(la,end=' ')
print(ra,end=' ')
print(w,end=' ')
print(rl,end=' ')
print(ll)


