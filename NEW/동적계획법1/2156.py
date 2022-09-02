import sys
n = int(sys.stdin.readline())
n_list = []
dp = []
for i in range(n):
    n_list.append(int(sys.stdin.readline()))
    if i==0:
        dp.append(n_list[0])
        continue
    if i==1:
        dp.append(n_list[0]+n_list[1])
        continue
    if i==2:
        dp.append(max(n_list[0]+n_list[1],n_list[0]+n_list[2],n_list[2]+n_list[1]))
        continue
    value = n_list[i] + max(dp[i-3]+n_list[i-1], dp[i-2])
    
    dp.append(max(value,dp[i-1]))
    
print(dp[n-1])
# 포도주를 2번 연속 안 먹을 경우가 존재한다.