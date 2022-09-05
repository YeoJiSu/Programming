import sys
A = list(sys.stdin.readline().split('\n')[0])
B = list(sys.stdin.readline().split('\n')[0])

dp = [[0 for i in range(len(A)+1)]for j in range(len(B)+1)]
for i in range(len(B)):
    for j in range(len(A)):
        if A[j] == B[i]:
            dp[i+1][j+1] = dp[i][j]+1
        else:
            dp[i+1][j+1] = max(dp[i+1][j],dp[i][j+1])

print(dp[len(B)][len(A)])
# 출처 : https://melonicedlatte.com/algorithm/2018/03/15/181550.html