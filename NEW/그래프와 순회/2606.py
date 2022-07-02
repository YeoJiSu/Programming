import sys
computer_count = int(sys.stdin.readline())
E = int(sys.stdin.readline())
edge=[[]for i in range(computer_count+1)]
for i in range(E):
    a,b = map(int, sys.stdin.readline().split(' '))
    edge[a].append(b)
    edge[b].append(a)
visited = [0 for i in range(computer_count+1)]
def dfs(R):
    visited[R]=1
    for x in edge[R]:
        if visited[x]==0:
            dfs(x)
dfs(1)
print(visited.count(1)-1)