'''
23:06

0. 문제 이해
수빈이는 현재 점 N(0 ≤ N ≤ 100,000)에 있고, 동생은 점 K(0 ≤ K ≤ 100,000)
X일 때 걷는다면 1초 후에 X-1 또는 X+1로 이동
순간이동을 하는 경우에는 0초 후에 2*X의 위치로 이동

출력 : 수빈이가 동생을 찾는 가장 빠른 시간을 출력한다

1. 아이디어
- 곱해진 것과, 더하고 곱한 것중 무엇이 더 가까운지 보면 돼.
- 이진수로 비트마스킹 같은데

'''
from collections import deque

n, k = map(int,input().split())

ans = [-1] * 100001

q = deque([n])
ans[n] = 0

while q :
    print(q)
    n = q.popleft()
    if n == k :
        break

    for nn in [n+1, n-1, 2 * n]:
        if 0<= nn <= 100000:
            if nn  == 2 * n :
                if ans[nn] == -1:
                    q.appendleft(nn)
                    ans[nn] = ans[n]
            else :
                if ans[nn] == -1 :
                    q.append(nn)
                    ans[nn] = ans[n] + 1


print(ans[k])
