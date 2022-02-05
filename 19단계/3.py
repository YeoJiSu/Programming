import sys
from collections import deque
def Josephus():
    N, K = map(int, sys.stdin.readline().split(" "))
    que = deque([i for i in range(1,N+1)])
    new_que=deque([]);
    while len(que)>0:
        que.rotate(-K+1)
        new_que.append(que.popleft())
    print("<",end="")
    print(*new_que,sep=", ",end=">\n")
if __name__=="__main__":
    Josephus()