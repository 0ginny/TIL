'''
13:51

'''
n = int(input())
m = list(map(int,input().split()))
m.sort()
print(sum([(n-i) * m[i] for i in range(n)]))