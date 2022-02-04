import sys
from collections import deque
def command():
    num = int(sys.stdin.readline())
    myque= deque([])
    for i in range(num):
        order = sys.stdin.readline().split("\n")[0]
        if order=="pop":
            if len(myque) == 0:
                print(-1)
            else:
                print(myque.popleft())
        elif order=="size":
            print(len(myque))
        elif order=="empty":
            if len(myque)==0:
                print(1)
            else:
                print(0)
        elif order=="front":
            if len(myque) == 0:
                print(-1)
            else:
                print(myque[0])
        elif order=="back":
            if len(myque) == 0:
                print(-1)
            else:
                print(myque[-1])
        else:
            order, num = order.split(" ")
            myque.append(num)
if __name__=="__main__":
    command()