from collections import deque

def bfs(graph, visit, start):
    queue = deque()
    queue.append(start)
    
    while queue:
        spot = queue.popleft()
        print(spot)
        visit[spot] = True
        for i in graph[spot]:
            if visit[i] == False:
                visit[i] = True
                queue.append(i)
    
graph = [
    [],
    [2,3,8],
    [1,7],
    [1,4,5],
    [3,5],
    [3,4],
    [7],
    [2,6,8],
    [1,7],
]
visit = [False]*9

bfs(graph,visit,1)

