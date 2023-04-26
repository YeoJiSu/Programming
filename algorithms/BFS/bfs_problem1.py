from collections import deque
import sys

N,M = map(int, sys.stdin.readline().split(' '))
graph = []
for i in range(N):
    graph.append(list(map(int, sys.stdin.readline().split('\n')[0])))
    
def neighbor(x,y,ice):
    li = []
    if x != 0 and ice[x-1][y] == 0:
        li.append([x-1,y])
    if x != N-1 and ice[x+1][y] == 0:
        li.append([x+1,y])
    if y !=0 and ice[x][y-1] ==0:
        li.append([x,y-1])
    if y !=M-1 and ice[x][y+1] == 0:
        li.append([x,y+1])
    return li

def bfs(ice, start):
    
    queue = deque()
    queue.append(start)
    
    ice_cream = False
    
    while queue:
        idx = queue.popleft()
        x = idx[0]
        y = idx[1]
        if ice[x][y] == 0:
            ice_cream = True
            ice[x][y] = 1
            li = neighbor(x,y,ice)
            for m in li:
                queue.append(m)
                
    return ice_cream        
    
        
    
count = 0
for y in range(M):
    for x in range(N):
        value = bfs(graph,[x,y])
        if  value == True:
            count+=1
print(count)
