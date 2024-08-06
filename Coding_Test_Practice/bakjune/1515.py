'''
시작 : 10:38


0. 문제이해
1 ~ N 까지 모든 수를 순차적으로 썼는데
지워진 결론만 보여
결론을 보고  최소 N 을 구해

한줄로 이어붙인 수 최대 3000 자리

1. 아이디어
구현 :
    보이는 내용에서 각 숫자들의 총 갯수가 같으면 돼.
    for 문을 3000 (넉넉하게) 까지 돌리면서 각 숫자들의 합을 구해
    그 합이 입력보다 크거나 같을 경우 그 값을 출력해
        검사할 때 시간복잡도는? 10 번씩 -> 10 : 3000

    맨 처음엔 count 10번 하면 돼 (count 시간복잡도는??)
    시간복잡도, 3000

-- 이 방법은 안돼. 문제가 숫자가 순차적으로 나오는게 기준이야.
진짜 연결했을 때, 입력의 부분집합들이 가능한지를 판단하면 안되나?
입력의 부분집합을 어떻게 나눌건데?

전체를 그냥 순서대로 list

모든 반례가 다 맞는데 왜 틀린지 모르겠다

----- 문제를 이해했을 때
입력에 없는 숫자를 모두 지웠다는 내용인듯

그럼 순서대로 다 더할때 해당 숫자가 있으면 전부 제거해.
그 값이 입력과 같으면 그 때의 cnt 를 출력해

이것도 아니야
-----

이전 꺼 반례 찾아보자

01

정답 11
출력 10
'''


import sys
from collections import deque

input = sys.stdin.readline

nlist = list(str(input().rstrip()))
# print(nlist)
cnt = 1
test = deque()

for n in nlist:

    if n in test :
        while 1:
            p = test.popleft()
            if p == n:
                break
        continue
    while 1:
        for j in list(str(cnt)):
            test.append(j)
        # print(test)
        cnt+=1
        if n in test:
            while 1 :
                p = test.popleft()
                if p == n :
                    break
            break

print(cnt-1)