'''
13:32


'''
import sys

input = sys.stdin.readline

n = int(input())
m = [int(input()) for _ in range(n)]
m.sort()
maxl = 0

for i in range(n):
    maxl = max((i+1) * m[-(i+1)] , maxl)

print(maxl)