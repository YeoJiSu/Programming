import sys
N = int(sys.stdin.readline())

dp = [1 for i in range(1000001)]
for i in range(2,1000001):
    dp[i] = (dp[i-1]+dp[i-2])%15746

print(dp[N])