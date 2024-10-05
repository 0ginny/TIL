'''
18:44

친구와 친구의 친구 까지만,
1에서 시작해서 bfs 로 깊이 2 까지만 초대
bfs의 깊이를 어떻게 측정하나?
    deque 로 했을 때,, 깊이도 같이 저장하면 될듯

'''

import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
m = int(input())

ms = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int,input().split())
    ms[a].append(b)
    ms[b].append(a)


cnt = 0
chk = [False] * (n+1 )
chk[1] = True
q = deque([(1,0)])

while q :
    (a,num) = q.popleft()
    if num >1 :
        continue
    # print(f'num {num}, q {q}, a {a}, ms {ms[a]}')

    for e in ms[a] :
        if chk[e] == False:
            chk[e] = True
            cnt += 1
            # print(f'add {e}')
            q.append((e,num+1))

print(cnt)