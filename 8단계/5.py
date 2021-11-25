import sys
import math
try: 
    count = int(sys.stdin.readline())
    for i in range(0,count):
        H,W,N = map(int, sys.stdin.readline().split(" "))
        num = N%H
        if num==0:
            num = H
        num = (num)*100+math.ceil(N/H)
        print(num)
except:
    exit()