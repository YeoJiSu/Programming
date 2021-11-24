import sys
import math
A,B,V = map(int,sys.stdin.readline().split(" "))

try:
    if V==0:
        print(0)
    else:
        days=1
        days+=math.ceil((V-A)/(A-B))
        print(days)

except:
    exit()

    