import sys
sys.setrecursionlimit(100000)
N, M, R = map(int, sys.stdin.readline().split(' '))
edge = [[] for i in range(N+1)]
for i in range(M):
    a,b = map(int, sys.stdin.readline().split(' '))
    edge[a].append(b)
    edge[b].append(a)
visited = [0 for i in range(N+1)]

count = 1
def dfs(R):
    global visited, edge, count
    visited[R] = count
    count+=1
    for x in sorted(edge[R], reverse=True):
        if visited[x] == 0:
            dfs(x)
dfs(R)
for i in range(1,N+1):
    print(visited[i])