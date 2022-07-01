import sys
sys.setrecursionlimit(100000)
N,M,R = map(int,sys.stdin.readline().split(' '))
visited = [0 for i in range(N+1)]
edge = [[] for i in range(N+1)]
V = [v for v in range(1,N+1)]
queue = []
index = 1

for i in range(M):
    a,b = map(int, sys.stdin.readline().split(' '))
    edge[a].append(b)
    edge[b].append(a)

def bfs(R):
    global visited,edge,V,queue,index
    for v in V:
        visited[v] = 0
    visited[R]= index
    index+=1
    queue.append(R)
    while True:
        if len(queue) == 0:
            break
        u = queue.pop(0)
        for v in sorted(edge[u], reverse=True):
            if visited[v] == 0:
                visited[v]=index
                index+=1
                queue.append(v)
bfs(R)
for i in range(1,N+1):
    print(visited[i])