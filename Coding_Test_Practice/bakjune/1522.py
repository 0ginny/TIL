'''
시작 21:24


'''

import sys

input = sys.stdin.readline

l = list(input().rstrip())

cnta = l.count('b')
ans = 0
if cnta > 0 :
    temp = l[-cnta:].count('a')
    ans = temp
    for i in range(len(l)):
        if l[i-cnta] == 'a' :
            temp -= 1
        if l[i] == 'a' :
            temp += 1
        ans = min(temp,ans)

print(ans)
