import sys
ENF = 1000000000
N= int(sys.stdin.readline())
dp = [[1 for k in range(10)] for i in range(100)]
dp[0][0] = 0
for i in range(1,100):
    for k in range(10):
        if k == 0:
            dp[i][k] = (dp[i-1][k+1])%ENF
            continue
        if k== 9:
            dp[i][k] = (dp[i-1][k-1])%ENF
            continue
        dp[i][k] = (dp[i-1][k-1]+dp[i-1][k+1])%ENF
print(sum(dp[N-1])%ENF)