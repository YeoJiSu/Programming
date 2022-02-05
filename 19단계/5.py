import sys
from collections import deque

def command():
    count = int(sys.stdin.readline())
    que = deque([])
    for i in range(count):
        order = sys.stdin.readline().split("\n")[0]
        if order=="pop_front":
            if len(que)==0:
                print(-1)
            else:
                print(que.popleft())
        elif order=="pop_back":
            if len(que)==0:
                print(-1)
            else:
                print(que.pop())
        elif order=="size":
            print(len(que))
        elif order=="empty":
            if len(que)==0:
                print(1)
            else:
                print(0)
        elif order=="front":
            if len(que)==0:
                print(-1)
            else:
                print(que[0])
        elif order=="back":
            if len(que)==0:
                print(-1)
            else:
                print(que[-1])
        else:
            order, num = order.split(" ")
            if order=="push_front":
                que.appendleft(num)
            elif order=="push_back":
                que.append(num)
if __name__=="__main__":
    command()