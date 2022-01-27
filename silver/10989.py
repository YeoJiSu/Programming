import sys
num = int(sys.stdin.readline())
a = [0]*10001
for i in range(0,num):
    num = int(sys.stdin.readline())
    a[num] +=1
for i in range(10001):
    if a[i]!=0:
        for k in range(a[i]):
            print(i)
