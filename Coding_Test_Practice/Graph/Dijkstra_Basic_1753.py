import sys
import heapq

input = sys.stdin.readline

V, E = map(int,input().split())
S = int(input())

el = [list(map(int,input().split())) for _ in range(E)]

