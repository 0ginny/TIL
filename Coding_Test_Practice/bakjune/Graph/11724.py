'''
시작 : 18:30

미니 스패닝 트리 아니야?

연결 요소의 갯수란, 독립적인 친구들이 몇개가 있는지
'''

import sys

input = sys.stdin.readline

N, M = map(int,input().split())

ms = [[] for _ in range(N+1)]

for _ in range(M):
    a,b = map(int,input().split())
    ms[a].append(b)
    ms[b].append(a)

chk = [False] * (N+1)


cnt = 0

for i in range(1,N+1):
    if chk[i] == False:
        chk[i] = True
        q = [i]
        cnt += 1
        while q:
            n =q.pop()
            for e in ms[n]:
                if chk[e] == False:
                    q.append(e)
                    chk[e] = True

print(cnt)