"""
시작 : 12:11
아이디어
- 결국 거리가 가장짧은 K개의 합 아닌가?
    - 다만 중복이 ㅇ벗어야 하는 거지.
- 일단 양옆의 회사를 연결하는 것이 가장 짧을 거야.
    - 우선 거리순으로 정렬
    - 1-2
    그리고 다음 1-2 2-3 중 어느것이 더 짧은지
    그리고 다음 1-2 + 3-4 와 2-3 어느것이 더 짧은지
    그리고 다음 1-2+ 3-4 와 1-2+4-5 와 2-3, 3-4 어느것이 더 짧은지.

    - 근데 문제는 k가 정해지지 않았어.

    - 일단은 전체 1-2 3-4 이런 식으로 k 개를 묶어.
        - 그리고 하나가 추가되었을 때. 어떻게 하지?
- 일단 맨 처음부터, 양옆과 비교해서 더 가까운 거리를 묶어.
    - 근데 k 가 부족하다?

"""