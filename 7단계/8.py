import sys
str = sys.stdin.readline().split("\n")[0]
sum=0
for i in str:
    count=2
    if i in "ABC":
        count+=1
    elif i in "DEF":
        count+=2
    elif i in "GHI":
        count+=3
    elif i in "JKL":
        count+=4
    elif i in "MNO":
        count+=5
    elif i in "PQRS":
        count+=6
    elif i in "TUV":
        count+=7
    elif i in "WXYZ":
        count+=8
    else:
        count+=0
    sum+=count
print(sum)