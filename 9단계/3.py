# 소인수분해 
import sys
import math
num = int(sys.stdin.readline())
index =2
while True:
    if num%index==0:
        print(index)
        num=math.trunc(num/index)
        if num==1:
            exit()
    else:
        index+=1
        if num==1:
            exit()
