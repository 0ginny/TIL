'''
시작 : 13:36

0. 문제 이해
보보는 1 ~~ n 의 라벨을 가지고 ㅣㅇㅆ어
i 번째 보보는 ai 캔디를 손에 쥐고 있어.
m 번의 라운드가 진행되고
    각 라운드에서 가장 적은 캔디를 가진 살마이 x 캔디를 받아
        단 가진 캔디수가 같다면 가장 적은 라벨이 상품을 받아
    1st 는 게임 시작 전에 최대 y 의 캔디를 가지고 시작해.
        그니까 이 말은 1번째 인원은 최종 계산을 할 때 y 개를 플러스 해서 계산을 하라는 거지?
            **** 아니야 그런 뜻이 아니라 첫번째 사탕은 n ~ n +y 일수 있다라는 거야.
                그럼 모든 경우를 다 비교해야 하나? 시간복잡도때문에 불가능해
                이게 영향을 전체에 다 끼치는 건가? 아니면 한번만 영향이 있는건가?
                0 1 2 3 4 5 에서 y = 5 라면 모든 케이스가 전체의 영향을 주겠네
                    이걸 어떻게 처리하지?
                        중요한 건 누가 최대인진 몰라도 최대로 몇개까지 가능한지 확인하는 거야.
                            여기서 중요한 건 최대의 가능성이 있는 친구가 최대로 이겨야하는거지
                                승자 판단 알고리즘
                                라운드 진행은 heap으로 하는게 맞아.
                                    근데 y 번 heap으로 돌리면 이것도 문제야.
                                    여기서 y 번이 아니라 적은 수로 하는 법을 결정해야해.
                                     일단 0과 y만 생각해보자

출력은 어떤 한 인원이 m 라운드 뒤에 최대 몇개의 캔디를 가질 수 있는지(가장 최대로 가질 수 있는 수)

1. 아이디어
- 구현
alist [사탕수]
전체 실행 2*e5

최소인 걸 어떻게 구할거야?
    전체 비교? 4* e10 불가능
    heap? 이건 전체 1번 실행하면서 최종 진행 가능 N * log N 가능
        숫자가 같은 경우도 가능했나?


'''
import heapq
import sys

input = sys.stdin.readline

n, m, x, y  = map(int,input().split())
heap = []
alist = list(map(int,input().split()))

# 최종 순위 확인
maxn = 0
for yy in range(y+1):
    heap = []
    for idx, num in enumerate(alist):
        if idx == 0 :
            num += yy
        heapq.heappush(heap,(num,idx))
    # 라운드 m 번 진행
    for _ in range(m):
        # 가장 작은 거 pop
        # print(heap)
        (n,i) = heapq.heappop(heap)
        heapq.heappush(heap,(n+x,i))

    max_list = max(heap)
    maxn = max(maxn,max_list[0])

print(maxn)

