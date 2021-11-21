import sys
# import collections
x=[]
y=[]
for i in range(0,2):
    a,b= map(int, sys.stdin.readline().split(" "))
    x.append(a)
    y.append(b)
a,b= map(int, sys.stdin.readline().split(" "))
if a not in x:
    print(a, end=" ")
else:
    if (a==x[0]):
        print(x[1], end=" ")
    else:
        print(x[0], end=" ")
    
if b not in y:
    print(b)
else:
    if (b==y[0]):
        print(y[1])
    else:
        print(y[0])
# count_x = collections.Counter(x).most_common[-1]
# count_y = collections.Counter(y).most_common[-1]
# print(count_x ,count_y)

    