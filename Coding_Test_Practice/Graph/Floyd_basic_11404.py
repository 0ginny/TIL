import sys
input = sys.stdin.readline
INF = sys.maxsize

n = int(input()) # city #
# bus #
m = int(input())
# a : b : c = 시작 : 도착 : 비용
# a == b 일 경우 c = 0

# fare first setting
fares = [[INF] * n for _ in range(n)]
for i in range(n) :
    fares[i][i] = 0
for _ in range(m):
    s, e, c = map(int,input().split())
    fares[s-1][e-1] = min(c, fares[s-1][e-1])

for v in range(n):
    for ss in range(n):
        for ee in range(n):
            if fares[ss][ee] > fares[ss][v] + fares[v][ee]:
                fares[ss][ee] = fares[ss][v] + fares[v][ee]

for str_list in fares:
    print(' '.join(list(map(str,str_list))))