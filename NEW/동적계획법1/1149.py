import sys
N = int(sys.stdin.readline())
cost = []
for i in range(N):
    cost.append(list(map(int, sys.stdin.readline().split(' '))))
    if i == 0:
        continue
    cost[i][0] += min(cost[i-1][1],cost[i-1][2])
    cost[i][1] += min(cost[i-1][0],cost[i-1][2])
    cost[i][2] += min(cost[i-1][0],cost[i-1][1])

print(min(cost[N-1]))