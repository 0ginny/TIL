
def solution(n):
    l = [[0] * n for _ in range(n)]

    di = [0 ,1 ,0 ,-1]
    dj = [1 ,0 ,-1 ,0]
    k = 0
    cnt = 1
    i, j = 0, -1

    while cnt <= n**2:
        ni = i + di[k]
        nj = j + dj[k]
        print(f'i : {i}, j : {j}, ni : {ni}, nj : {nj}, cnt : {cnt}')
        if 0<= ni < n and 0 <= nj < n and l[ni][nj] == 0:
            l[ni][nj] = cnt
            cnt += 1
            i, j = ni, nj
        else:
            if k < 3:
                k += 1
            else:
                k = 0
    return l

print(solution(4))