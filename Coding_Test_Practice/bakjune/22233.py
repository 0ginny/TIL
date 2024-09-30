'''
시작 : 10:50

0. 문제이해
 메모장에 써진 키워드는 모두 서로 다르며, 총 N개가 존재
 새로운 글을 작성할 때, 최대 10개의 키워드에 대해서 글을 작성
 키워드는 가희가 글을 쓴 이후, 메모장에서 지워지게 됩니다.
  글을 쓰고 나서, 메모장에 있는 키워드 개수가 몇 개인지 알고 싶습니다

- 입력 :
첫 번째 줄에 가희가 메모장에 적은 키워드 개수 N, 가희가 블로그에 쓴 글의 개수 M
2번째 줄부터 N+1번째 줄까지 메모장에 적은 키워드 N개
N+2번째 줄부터 N+M+1번째 줄까지, 가희가 쓴 글과 관련된 키워드,  (쉼표)로 구분

- 출력 :
x번째 줄에는 x번째 글을 쓰고 난 후에 메모장에 남아 있는 키워드의 개수를 출력해 주세요.

- 조건
1 ≤ N ≤ 2×105
1 ≤ M ≤ 2×105
1 ≤ 글에 있는 키워드 개수 ≤ 10
1 ≤ 키워드 길이 ≤ 10
키워드는 소문자와 숫자로만 이루어져 있습니다.
메모장에 있는 키워드 이름은 중복되지 않습니다.
글에 있는 키워드 이름은 중복되지 않습니다. 그러나, 한 키워드는 여러 글에 있을 수 있습니다
        키워드를 제거만 하면 될 듯.

1. 아이디어
- 구현
    - 메모장 리스트 작성
    - 글 쓰기 전에 리스트 카피
    - 글을 쓰며 remove ( len(N)) * 10 )
    - 시간복잡도 N * 10 * M 시간 초과

- remove 보다 set 에 저장하고 차집합 후 len(set) 하면 될듯
N + M 가능

'''

import sys

input = sys.stdin.readline

N, M = map(int,input().split())

memo = set()
for _ in range(N):
    memo.add(input().rstrip())

ans = []
for _ in range(M):
    assay = set(list(input().rstrip().split(',')))
    memo -= assay
    ans.append(len(memo))

for a in ans:
    print(a)