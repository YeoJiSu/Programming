import sys
sys.setrecursionlimit(100000)
N,M,R = map(int, sys.stdin.readline().split(' '))
E = [[] for _ in range(N+1)]
for i in range(M):
    u,v = map(int, sys.stdin.readline().split(' '))
    E[u].append(v)
    E[v].append(u)


visited = [0 for _ in range(N+1)]
order = 1
def dfs(E, R):
    global order
    global visited
    visited[R] = order
    order+=1
    for x in sorted(E[R]):
        if visited[x]==0:
            dfs(E,x)
dfs(E,R)
for i in range(1,N+1):
    print(visited[i])
