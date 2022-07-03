import sys
N = int(sys.stdin.readline())
dx = [0,0,1,-1]
dy = [1,-1,0,0]
arr = []
for i in range(N):
    arr.append(list(sys.stdin.readline().split('\n')[0]))

def bfs(x,y):
    global N, arr,dx,dy
    arr[x][y]='0' # 방문했으니 0으로 바꿔두기
    queue = []
    queue.append((x,y))
    count = 1
    while queue:
        a,b = queue.pop(0)
        for i in range(4):
            new_x = a + dx[i]
            new_y = b + dy[i]
            if new_x<0 or new_x>=N or new_y<0 or new_y>=N:
                continue
            if arr[new_x][new_y]=='1':
                arr[new_x][new_y]='0'
                queue.append((new_x,new_y))
                count+=1
    return count

count_arr = []
for i in range(N):
    for j in range(N):
        if arr[i][j]=='1':
            count_arr.append(bfs(i,j))
print(len(count_arr))
for i in sorted(count_arr):
    print(i)