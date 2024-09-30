import sys

target = int(sys.stdin.readline())
n = 1
ans = [0] * 46
ans[0] = 0
ans[1] = 1
ans[2] = 2
for n in range(2,target+1):
    ans[n] = ans[n-1] + ans[n-2]

print(ans[target])