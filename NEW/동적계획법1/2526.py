import sys
n = int(sys.stdin.readline())
n_list = []

for i in range(n):
    n_list.append(list(map(int, sys.stdin.readline().split(' '))))
n_list.sort()

dp = [1 for i in range(n)]
for i in range(n):
    for j in range(i):
        if n_list[j][1] < n_list[i][1]:
            dp[i] = max(dp[i],dp[j]+1)
print(n-max(dp))