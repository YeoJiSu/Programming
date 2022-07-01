from operator import index
import sys
sys.setrecursionlimit(1000)
N,M,R = map(int, sys.stdin.readline().split(' '))
visited_bfs = [0 for i in range(N+1)]
visited_dfs = [0 for i in range(N+1)]
edge=[[]for i in range(N+1)]

index_bfs = 1
queue = []

for i in range(M):
    a,b = map(int, sys.stdin.readline().split(' '))
    edge[a].append(b)
    edge[b].append(a)

dfs_list = []
def dfs(R):
    global visited_dfs, edge, dfs_list
    visited_dfs[R] = 1
    dfs_list.append(R)
    for x in sorted(edge[R]):
        if visited_dfs[x] == 0:
            dfs(x)
dfs(R)
for i in dfs_list:
    print(i, end=" ")
print()
bfs_list = []
def bfs(R):
    global visited_bfs, bfs_list, queue, edge
    for i in range(N+1):
        visited_bfs[i]=0
    visited_bfs[R]=1
    bfs_list.append(R)
    queue.append(R)
    while True:
        if len(queue) == 0:
            break
        u = queue.pop(0)
        for x in sorted(edge[u]):
            if visited_bfs[x]==0:
                visited_bfs[x]=1
                queue.append(x)
                bfs_list.append(x)
bfs(R)
for i in bfs_list:
    print(i, end=" ")