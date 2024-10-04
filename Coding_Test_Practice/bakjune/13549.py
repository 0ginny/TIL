'''
23:06

0. 문제 이해
수빈이는 현재 점 N(0 ≤ N ≤ 100,000)에 있고, 동생은 점 K(0 ≤ K ≤ 100,000)
X일 때 걷는다면 1초 후에 X-1 또는 X+1로 이동
순간이동을 하는 경우에는 0초 후에 2*X의 위치로 이동

출력 : 수빈이가 동생을 찾는 가장 빠른 시간을 출력한다

1. 아이디어
- 곱해진 것과, 더하고 곱한 것중 무엇이 더 가까운지 보면 돼.
- 이진수로 비트마스킹 같은데

'''


# print(str(bin(5<<2 ^ 16)).count('1'))


n, k = map(int,input().split())

ans = 100000
if k > n :
    temp = str(bin(n ^ k)).count('1')
    ans = min(temp, ans)
    while k >= n :
        n <<= 1
        temp = str(bin(n ^ k)).count('1')
        ans = min(temp,ans)


else :
    ans = n-k

print(ans)