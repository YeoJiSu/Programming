import sys
import itertools
N = int(sys.stdin.readline())
team = []
arr = [ i for i in range(N) ]
for i in range(N):
    team.append(list(map(int, sys.stdin.readline().split(' '))))

comb = list(map(tuple, itertools.combinations(arr,N//2)))
half = comb[:len(comb)//2]
half2 = comb[len(comb)//2:]
del comb
min_value = 1e9

for index in range(len(half)):
    line = half[index]
    line2 = half2[len(half2)-1 - index]
    first = 0
    second = 0
    for x in range(len(line)):
        for y in range(len(line)):
            if x!=y:
                first += team[line[x]][line[y]]
                second += team[line2[x]][line2[y]]
    min_value = min(min_value, abs(first-second))
   
print("브루트포스로 푼 결과:",min_value)

# 백트레킹으로 풀기
min_value = 1e9
visited = [0 for i in range(N)]
def dfs(depth, i):
    global team, min_value
    first = 0
    second = 0
    if depth == N//2 :
        for x in range(N):
            for y in range(N):
                if x!=y:
                    if visited[x] == 1 and visited[y]==1:
                        first+=team[x][y]
                    if visited[x] == 0 and visited[y]==0:
                        second+=team[x][y]
        min_value = min(min_value, abs(first-second))
    for k in range(i,N):
        if visited[k] == 0:
            visited[k] = 1
            dfs(depth+1,k+1)
            visited[k] = 0

dfs(0,0)

print("백트레킹으로 푼 결과:",min_value)
