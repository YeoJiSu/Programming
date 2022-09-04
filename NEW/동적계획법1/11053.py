import sys
N = int(sys.stdin.readline())
n_list = list(map(int, sys.stdin.readline().split(' ')))
dp = [1 for i in range(N)]
for i in range(N):
    for j in range(i):
        if n_list[i] > n_list[j]:
            dp[i] = max(dp[i],dp[j]+1)
print(max(dp))