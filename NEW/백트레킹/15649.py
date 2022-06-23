# N과 M(1)
import sys
N,M = map(int,sys.stdin.readline().split(' '))
visit = [0]*N
seq = [0]*M
def recursive(x):
    if x==M:
        for i in seq:
            print(i, end=" ")
        print()
        return
    for i in range(N):
        if visit[i]==0:
            visit[i]=1
            seq[x]=i+1
            recursive(x+1)
            visit[i]=0 
recursive(0)