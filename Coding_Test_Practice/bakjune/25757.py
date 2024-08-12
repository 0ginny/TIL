'''
시작  ;9:58
종료 : 10:07
0. 문제 이해

'''

import sys

input = sys.stdin.readline

N, G = input().split()
N = int(N)
s = set()

for _ in range(N):
    s.add(input().rstrip())

num = len(s)

def ans(num,G) -> int :
    if G == 'Y':
        return num
    elif G == 'F':
        return num // 2
    else :
        return num // 3

print(ans(num,G))