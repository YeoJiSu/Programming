import sys
from queue import Queue
from collections import deque
def card_game_using_queue():
    num = int(sys.stdin.readline())
    que = Queue()
    for i in range(num):
        que.put(i+1)
    while que.qsize()>1:
        que.get()
        up = que.get()
        que.put(up)
    print(que.get())
def card_game_using_deque():
    num = int(sys.stdin.readline())
    que = deque([i for i in range(1,num+1)])
    while len(que)>1:
        que.popleft()
        up = que.popleft()
        que.append(up)
    print(que.pop())
if __name__=="__main__":
    card_game_using_deque()
