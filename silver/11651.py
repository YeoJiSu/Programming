import sys
num = int(sys.stdin.readline())
my_list=[]
for i in range(num):
    x,y = map(int, sys.stdin.readline().split(' '))
    my_list.append([y,x])
my_list.sort(reverse=False)
for i in my_list:
    print(i[1],i[0])