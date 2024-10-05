'''
13:56

0. 문제이해
- 조건을 만족하는 최소 꽃

3/1 ~ 11/30 까지 모든 곳을 채워야해

- 입력 :
    N  (1 ≤ N ≤ 100,000)
    sm sd em ed


1. 아이디어
어차피 최소 꽃의 '수'야. 그러니까 끝을 기준으로,
정렬을
    끝이 긴거, 시작 앞에거
1. 처음에 3/1 이전에 시작하는 꽃이 있는지 확인 없으면 종료 1번 순환
    그거 기준으로 last 리뉴얼
2. for 문 돌면서 last >= st 인 걸로 last 리뉴얼 2번째
3. 만약 last < 11/30 인데 for 문을 다 돌았을 때 리뉴얼이 안된다? 그럼 종료
4. 만약 last 11/ 30 이상이면 종료

'''

import sys
input = sys.stdin.readline

n = int(input())
fs = [list(map(int,input().split())) for _ in range(n)]

fs.sort(key = lambda x : (-x[2],-x[3],x[1],x[0]))
# print(fs)
chk = False
cnt = 0
last = [0,0]
for i,f in enumerate(fs):
    if f[0] < 3 or f[0] ==3 and f[1] == 1: # 3월 1일은 포함이 안되었어...
        chk = True
        last = f[2:]
        fs = fs[:i]
        cnt += 1
        # print('1' ,last)
        break
# print(fs)
def dfs():
    global last,fs, cnt
    print('last',last)
    print(fs)
    for i,f in enumerate(fs) :
        # print(f)
        if last[0] > f[0] or (last[0] == f[0] and last[1]>= f[1]):
            last = f[2:]
            cnt += 1
            fs = fs[:i]
            return True
    return False
if 2<last[0]<12: # while 로 했을 때 한번에 종료 되어야 했는데 그걸 놓쳤어.
    while dfs() :
        if last[0] >= 12 :
            break
if last[0] >= 12 :
    print(cnt)
else :
    print(0)