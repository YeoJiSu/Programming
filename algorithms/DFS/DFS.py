from collections import deque

def dfs(graph, visit, start , queue):
    queue.append(start)
    visit[start] = True
    
    while queue:
        spot = queue.popleft()
        print(spot)
        for i in graph[spot]:
            if visit[i] == False:
                dfs(graph, visit, i,queue)

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
queue = deque()

dfs(graph,visit,1, queue)