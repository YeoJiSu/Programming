import sys
sys.setrecursionlimit(100000)
N,M,R = map(int, sys.stdin.readline().split(' '))
E = [[] for i in range(N+1)]
V = [i for i in range(1,N+1)]
visited = [0 for _ in range(N+1)]

for i in range(M):
    a,b = map(int, sys.stdin.readline().split(' '))
    E[a].append(b)
    E[b].append(a)

queue = []
index =1
def bfs(R):
    global E, V, visited, queue,index
    for v in V:
        visited[v]=0
    visited[R]=index
    index+=1
    queue.append(R)
    while True:
        if len(queue)==0:
            break
        u = queue.pop(0)
        for v in sorted(E[u]):
            if visited[v]==0:
                visited[v]=index
                index+=1
                queue.append(v)
bfs(R)
for i in range(1,N+1):
    print(visited[i])