import sys
num = int(sys.stdin.readline())
for i in range(0,num):
    print(" "*(num-i-1)+"*"*(i+1))