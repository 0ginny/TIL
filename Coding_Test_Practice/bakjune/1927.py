'''
시작 : 11:08

0. 문제이해
최소 힙을 이용하여 다음과 같은 연산을 지원하는 프로그램을 작성
    - heap 을 사용하는 예제인가봐
배열에 자연수 x를 넣는다.
배열에서 가장 작은 값을 출력하고, 그 값을 배열에서 제거한다.

- 입력 :
첫째 줄에 연산의 개수 N(1 ≤ N ≤ 100,000)
다음 N개의 줄에는 연산에 대한 정보를 나타내는 정수 x
     x가 자연수라면 배열에 x라는 값을 넣는(추가하는)
     x가 0이라면 배열에서 가장 작은 값을 출력하고 그 값을 배열에서 제거

     x는 231보다 작은 자연수 또는 0
- 출력
 0이 주어진 횟수만큼 답을 출력

1. 아이디어
heap
가중치를 최소 출력이니까 가중치를 그대로 써도 괜찮음.
0 이 입력되면 heappop 해서 ans 에 저장

힙의 시간적합도를 찾아보기 NlogN


'''
import sys
import heapq

input = sys.stdin.readline

N = int(input())
heap = []
ans = []
for _ in range(N):
    n = int(input())
    if n == 0 :
        if heap: # 값 존재
            h = heapq.heappop(heap)
            ans.append(h)
        else :
            ans.append(0)
    else : # n 이 자연수
        heapq.heappush(heap,n)

for a in ans :
    print(a)


