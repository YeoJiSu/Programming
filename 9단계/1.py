import sys
num = int(sys.stdin.readline())
my= list(map(int,sys.stdin.readline().split(" ")))
count = num
for i in range(0, num):
    if my[i]==1:
        num-=1
    elif my[i]==2 or my[i]==3:
        num=num
    else:
        for j in range(2,my[i]-1):
            if my[i]%j==0:
                num-=1
                break
print(num)

