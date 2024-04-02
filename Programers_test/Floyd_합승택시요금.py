import sys
INF = sys.maxsize


def solution(n, s, a, b, fares):
    answer = INF

    # fares list create
    fl = [[INF] * (n+1) for _ in range(n+1)]
    for i in range(1,n+1):
        fl[i][i] = 0
    for (A,B,f) in fares:
        fl[A][B] = min(f,fl[A][B])
        fl[B][A] = min(f,fl[A][B])

    #Floyd Argorithm
    for vv in range(1,n+1):
        for ss in range(1,n+1):
            for ee in range(1,n+1):
                if fl[ss][ee] > fl[ss][vv] + fl[vv][ee]:
                    fl[ss][ee] = fl[ss][vv] + fl[vv][ee]

    # debuging
    for l in fl:
        print(l[1:])
    print()

    # answering
    for vvv in range(1,n+1):
        print(f' v : {vvv}, answer : {answer}, {fl[s][vvv]} + {fl[vvv][a]} + {fl[vvv][b]}')
        answer = min(fl[s][vvv] + fl[vvv][a] + fl[vvv][b] , answer)

    return answer