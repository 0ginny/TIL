'''
12:50


'''

import sys

input = sys.stdin.readline

n = int(input())
m = [list(map(int,input().split())) for _ in range(n)]

chk = [False] * (max(m)[1]+1)

m.sort(key = lambda x : (x[1],x[0]))

cnt = 0
last = 0
for a in m :
    if a[1] >= last:
        if a[0] >= last:
            last = a[1]
            cnt += 1

print(cnt)