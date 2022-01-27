import sys
num=int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split(" ")))
length = len(a)
sum = 0
for i in sorted(a):
    sum+=i*length
    length-=1
print(sum)