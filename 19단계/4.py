import sys
from collections import deque
def printer():
    num = int(sys.stdin.readline())
    for i in range(num):
        N, M = map(int,sys.stdin.readline().split(" "))
        que = deque(list(map(int,sys.stdin.readline().split(" "))))
        index = list(range(0,N))
        index[M] = "goal"
        
        sequence = 0
        while len(que)>0:
            if que[0]==max(que):
                sequence+=1
                if index[0]=="goal":
                    print(sequence)
                    break
                else:
                    index.pop(0)
                    que.popleft()                
            else:
                que.append(que.popleft())
                index.append(index.pop(0))
        
        
if __name__ == "__main__":
    printer()