import sys
N = int(sys.stdin.readline())
n_list = list(map(int, sys.stdin.readline().split(' ')))
dp = [1 for i in range(N)]
for i in range(0,N):
    for j in range(0,i):
        if n_list[i] > n_list[j]:
            dp[i] = max(dp[i],dp[j]+1)
dp2 = [1 for i in range(N)]
for i in range(N-1,-1,-1):
    for j in range(N-1,i,-1):
        if n_list[i] > n_list[j]:
            dp2[i] = max(dp2[i],dp2[j]+1)
_sum = (dp[0]+dp2[0])-1
for i in range(1,N):
    _sum = max(_sum,(dp[i]+dp2[i])-1)
print(_sum)