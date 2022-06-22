import sys
num = 0
count = 0
board = []
visit = []

def main():
    global num,board,visit
    num = int(sys.stdin.readline())
    board = [0]*num
    visit = [False]*num
    dfs(0)
    print(count)
    
def dfs(x):
    global count
    if x == num:
        count+=1
        return 
    for i in range(num):
        if visit[i]==False:
            board[x]=i
            if isAvailable(x):
                visit[i]=True
                dfs(x+1)
                visit[i]=False
                
def isAvailable(x):
    for i in range(x):
        if board[x] == board[i] or abs(board[x]-board[i]) == x-i:
            return False
    return True

main()