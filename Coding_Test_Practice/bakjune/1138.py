'''
시작 : 1048
종료 : 1113

0. 문제 이해
- 사람들은 자기보다 큰 사람이 왼쪽에 몇 명 있었는지만을 기억
N명의 사람이 있고, 사람들의 키는 1부터 N까지 모두 다르다. - 1 ~ N 까지 있는 거야.
각 사람들이 기억하는 정보가 주어질 때, 줄을 어떻게 서야 하는지 출력

- 입력:
첫째 줄에 사람의 수 N이 주어진다. N은 10보다 작거나 같은 자연수
둘째 줄에는 키가 1인 사람부터 차례대로 자기보다 키가 큰 사람이 왼쪽에 몇 명이 있었는지
    i는 0부터 시작

- 출력 : 줄을 선 순서대로 키 나열

1. 아이디어
- an >= i (0 부터 시작)
- 그리디?? 큰 수부터 채워 넣으면 가능한가?
    - 큰수부터 채워 넣고, i 만큼 뒤로 가서 삽입 (insert)

'''


import sys

input = sys.stdin.readline

N = int(input())

ilist = list(map(int,input().split()))
ans = []
for n, i in reversed(list(enumerate(ilist))):
    ans.insert(i,n+1)

print(' '.join(list(map(str,ans))))
