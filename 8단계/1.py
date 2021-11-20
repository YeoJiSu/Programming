import sys
import math
try:
    value  = (sys.stdin.readline().split("\n")[0])
    a,b,c = map(int, value.split(" "))

    if (c-b)<=0:
        print(-1)
    else:
        run = math.floor(a/(c-b))
        print(run+1)
except:
    exit()