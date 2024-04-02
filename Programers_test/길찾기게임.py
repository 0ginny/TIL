"""
시작 : 3 : 40
- 10000 개의 노드가 있음 (x,y) 좌표
- 트리 구성 방법
    - y => 레벨을 나타내
    - x ,, 서로 다른 x값
    - y 값에 따라 부모 자식이 결정 되겠네 : 부모 > 자식
    - 이진 트리
- 전회순회
    - 맨 위부터 왼쪽 아래 끝 닿은 후, 왼쪽 중 오른쪽 이런 느낌
- 후회 순회
    -맨 왼쪽 말단 부터, 이짙프리가 있으면 다음 말단
- 이진트리를 어떻게 만들어야 할까?
    - 이진 구조라 heap을 쓰면 좋을 거 같은데, 가중치를 어떻게 구하지? 가중치랄게 있나? x좌표로 하면 되는 거 ㄱ아니야?
        - 안돼 heap은 완전이진트리라 지금과는 달라.
    - 일단 기준값은 정해지네, y 가장 위부터 아래로 가면서 서브가 정해져.
- 굳이 이진트리를 만들지 않고 그냥 답만 도출해도 되는 거 아닌가?

- 답만 도출할 경우
    - 전위 순회
        - y기준 가장 위, y 두번째 중 왼쪽, 3번째중 왼쪽,
        -recur 로 할 만 한데?
            - deque 를 써.
                - y가 가장 큰 거
                    -다음 중 x 작은 것 먼저.
                    내가 원하는 넣는 방식
                     7-4-6-9 ///여기를 어떻게 구분하지?
                      왼쪽이 없는 경우 위로 올라가서 오른쪽을 봐
                      -1-8-5-
                      node dict { (x,y) : n , ...}
                      level 별로 나누자 level[y] = [x ...]

                      아니다 각 노드에 서브 노드를 다 만들어서 dict에 넣으면 되잖아.
"""

nl  =[[5,3],[11,5],[13,3],[3,5],[6,1],[1,3],[8,6],[7,2],[2,2]]

def solution(nl):
    answer = [[]]
    level = [[] for _ in range(len(nl))]
    nd = {}
    mat = {}
    for num in range(len(nl)):
        nd[num] = [[],[]]
    for i,(x,y) in enumerate(nl):
        mat[x] = i
        level[y].append(x)

    print(level)
    print(mat)
    print(nd)
    for r in range(len(nl)):
        if level[-r]:
            if a
    # making binary tree





    return level[-1]

solution(nl)