'''
시작 : 4: 10
0. 문제 이해
    - 입력 : 이미 정점으로 연결을 한 상태
    - 출력 : 정점, 도넛그래프 수, 막대그래프 수, 8자 그래프 수
    - 그래프는 적어도 2개 이상이어야 해.

    - 각 그래프으 조건 :
        - 도넛 , 간선을 가다보면 자기 자신으로 돌아옴.
        - 막대 : 그냥 1자 연결 (node == edge 겠지? 연결이 되어있으니까.
        - 8자 , 도넛 2개야. 근데 노드 1개가 빠졌어.
1. 아이디어
    - 간선이 많아서 재귀도 어려워.
    - 정점 : 자신에게 오는 것이 없는 점. 그리고 나가는 것만 있는 점.
    - 일단 정점을 찾는다.
        - 노드 정리할 때 tset 에는 모든 노드 넣고
            - dset 에는 도착 노드만 넣어.
            - tset - dset 인 노드가 정점
        - nd = { node : [[이전노드], [다음 노드] }로 정리
    - 정점 기준 다음 노드 가서 그 노드 끝까지 진행. 그 중 2개 이상 한 노드에 연결되어 있으면 8자에  ad[8] 에 값 추가.
        - 계속 가는데 시작 노드를 거친다. ad[d] += 1
        - 계속 가는데 아무것도 없는 노드가 있다? ad[b] += 1
            - 단 막대일 때는 자신으로 오는 막대도 고려해서 갯수를 새야하네.

'''

edges = 	[[2, 1], [1, 3], [2, 4], [4, 5], [2, 6], [6, 7]]

def solution(edges):
    # 정점 찾기
    ts = set()
    ds = set()
    nd = {}
    for (s,e) in edges:
        ts.add(s)
        ts.add(e)
        ds.add(e)
    for n in ts:
        nd[n] = []
    for (s,e) in edges:
        nd[s].append(e)
    print(nd)
    # 정점
    for nn in ts - ds:
        if len(nd[nn]) >= 2 :
            basic = nn

    # 정답지 생성
    ans = [basic, 0, 0, 0]
    print(nd[2])
    # 정점에서 간선 연결
    for ex in nd[basic]:
        print('ex : ', ex)
        if nd[ex] : # 다음 노드가 있는 경우
            nex = ex
            print(f'nex : {nex}')
            while 1 : # 다음 노드가 있을 때까지 만약 끝까지 간다면 막대
                print(f' nex : {nex}, nd[nex] : {nd[nex]}, ans : {ans}')
                if not nd[nex] : # 노드 없으면 막대
                    ans[2] += 1
                    break
                if len(nd[nex]) > 1  : # 다음 간선이 2개가 넘으면 8자
                    ans[3] += 1
                    break
                if nd[nex][0] == ex : # 다음 간선이 최초의 간선이면 도넛
                    ans[1] += 1
                    break
                nex = nd[nex][0]
        else : # 노드 없으면 막대
            ans[2] += 1
    return ans

print(solution(edges))