'''
시작 : 10:37

0. 문제이해
- 남학생은 스위치 번호가 자기가 받은 수의 배수이면, 그 스위치의 상태를 바꾼다
- 여학생은 자기가 받은 수와 같은 번호가 붙은 스위치를 중심으로 좌우가 대칭이면서 가장 많은 스위치를 포함하는 구간을 찾아서, 그 구간에 속한 스위치의 상태를 모두 바꾼다.

입력 :
- N : 스위치 개수 ( 100 이하 양수)
- 스위치 상태 : ' ' 으로 구분
- P : 학생수
- g n : 성별(1 남성, 2 여성) 받은 번호


1. 아이디어
구현 :
    각 남학생, 여학생 작동 함수를 만들어서 구현
'''

import sys

input = sys.stdin.readline

N = int(input())
switch = list(map(int,input().split()))

P = int(input())


def swap(i):
    if i :
        i = 0
    else :
        i = 1
    return i

def manf(n):
    first = n
    while n <= N:
        switch[n-1] = swap(switch[n-1])
        n += first

def womanf(n):
    switch[n-1] = swap(switch[n-1])
    for i in range(1,N):
        if n-i > 0  and n+i <= N:
            if switch[n-i-1] == switch[n+i-1]:
                number = swap(switch[n + i - 1])
                switch[n + i - 1] = number
                switch[n - i - 1] = number
            else : break
        else : break


for _ in range(P):
    g, n = map(int,input().split())
    if g == 1 :
        manf(n)
    else :
        womanf(n)

for i,s in enumerate(switch):
    if (i +1) % 20 == 0:
        print(s)
    else:
        print(s,end= ' ')



