'''
시작 : 11:28

왼쪽이든 오른쪽이든 블루와 레드를 나누기만 하는 최소 이동 횟수
한 번에 이동 시킬 수 있어.

이거 그냥 색이 달라지는 횟수 -1 /2 하면 되는 거 아닌가?
'''

import sys

input = sys.stdin.readline

N = int(input())
balls = input().rstrip()
cnt = 0
for i in range(1,N):
    if balls[i-1] != balls[i] :
        cnt += 1

print(int(cnt/2))