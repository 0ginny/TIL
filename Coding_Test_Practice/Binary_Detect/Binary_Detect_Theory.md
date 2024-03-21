# 이진탐색
- 절반씩 나눠서 탐색
- 시간복잡도 : N -> logN 으로 감소

### 시간복잡도
N의 범위 500 인 경우 : O(N³) 알고리즘을 설계하면 문제를 풀 수 있다.

N의 범위 2,000 인 경우 : O(N²) 알고리즘을 설계하면 문제를 풀 수 있다.

N의 범위 100,000 인 경우 : O(NlogN) 알고리즘을 설계하면 문제를 풀 수 있다.

N의 범위 10,000,000 인 경우 : O(N) 알고리즘을 설계하면 문제를 풀 수 있다.

## 기본 코드
```
def search(st, en, target) :
    if st == en:
        # 여기에 원하는 완료조건
        return
    mid = (st+en) //2
    if nums[mid] < target:
        search(mid+1, en,target)
    else :
        search(st,mid,target)
```

