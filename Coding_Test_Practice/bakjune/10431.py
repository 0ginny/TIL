'''
시작 10:55
정지 11:13
재시작 : 12:00
완료 : 12:04

총 걸린 시간 : 22분

1. 아이디어
- 구현 :
    - 아무 순서대로 list
    - 앞 index 부터 1명씩 자신 앞리스트와 비교해서 큰 숫자가 있으면 자신보다 큰 수 앞으로 이동
    - 그렇게 이동시 이동한 만큼 cnt++
    - 총 몇번 움직였는지 출력
2. 시간복잡도
    - 이전에 자신보다 큰 키가 있는지 확인 :
        1~ 1000 까지의 합 e6
    - test 20 : e7 가능
'''

import sys

input = sys.stdin.readline


N = int(input())
lines = []
for _ in range(N):
    line = list(map(int,input().rstrip().split()))
    lines.append(line[1:])

for idx, line in enumerate(lines):
    apply = []
    cnt = 0
    for height in line:
        chk = False
        for i,num in enumerate(apply):
            if num > height:
                cnt += len(apply[i:])
                apply.insert(i,height)
                chk = True
                break
        if chk == False:
            apply.append(height)

    print(f'{idx+1} {cnt}')

