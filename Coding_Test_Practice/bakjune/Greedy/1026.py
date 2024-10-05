'''
13:42

어차피 덧셈인데 B를 재배열 안해도 똑같은 거 아니야?

낮은 순서와 높은 순서를 곱하는게 최소야
'''
import sys

input = sys.stdin.readline

n = int(input())
A = list(map(int,input().split()))
B = list(map(int,input().split()))

A.sort()
B.sort(reverse= True)

S = 0
for i in range(n):
    S += A[i] * B[i]

print(S)