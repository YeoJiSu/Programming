import sys
import math
N, W, H = map(int,sys.stdin.readline().split(" "))

C = int(math.sqrt(W**2+H**2))
for i in range(N):
    value = int(sys.stdin.readline())
    if (value <= C):
        print("DA")
    else:
        print("NE")