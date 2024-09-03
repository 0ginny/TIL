'''
시작 : 400
종료 : 502

0. 문제 이해

- N×N의 표에 수 N2개 채워져 있다. 채워진 수에는 한 가지 특징이 있는데, 모든 수는 자신의 한 칸 위에 있는 수보다 크다
N번째 큰 수를 찾는 프로그램을 작성

- 입력
첫째 줄에 N(1 ≤ N ≤ 1,500)

- 출력
N 번째 큰 수를 구하기

1. 아이디어
- 전체 숫자비교 가능? 전체 수 T = 1500 * 1500 = 1000000
    - 정렬 TlogT 가능하긴 한데?
시간복잡도는 되지만, 메모리 초과가 일어나, 그래서 배열의 크기를 정해서 값을 변경해도 메모리 초과가 일어나
------
- 적어도 N- i 행에 있는 수는 큰수가 i 개 이상은 있는 거야. 그럼 이 부분을 제거하자.
    - 그럼 어차피 처음부터네..
- 그럼 반대로 첫번째 줄에서 는 가장 큰 수만 가능
    - 두번째에선 큰 순으로 2개가 가능해.
    - 이런식으로 하면 메모리를 절반을 줄일 수 있지만, 시간복잡도가 추가되겠지.
    - ST = N * N /2 = e6
    - 이렇게 해도 메모리 초과야.
----------------
- all 의 최대갯수를 N 개로 한정해,
- 그리고 heap 자료구조로, pop 으로 최소값을 정하고,
    - 최소값보다 작은 값이 있다면, 그 값을 푸시해
- 중간에 틀렸대..
- 중복 숫자를 고려 안한 거 같아.
-26% 에서 틀려..
-- minn 을 푸시 후 동시에 팝 해서 해결 
-- naneerror가 생겼어
    -- minn 이 없는 경우?? N == 1 일때는 minn 없어.
'''

import sys
import heapq


input = sys.stdin.readline

N = int(input())
minh = []
chk = False
cnt = 0
for i in range(N):
    temp = list(map(int,input().split()))
    for a in temp:
        cnt += 1
        if cnt <= N :
            heapq.heappush(minh,a)
        else :
            if chk == False :
                minn = heapq.heappop(minh)
                chk = True
            if minn <= a :
                heapq.heappush(minh,a)
                minn = heapq.heappop(minh)

if N != 1 :
    print(minn)
else :
    print(a)