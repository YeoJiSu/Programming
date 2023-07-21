# 백준 14215번 - 세 막대
import sys
a,b,c = map(int, sys.stdin.readline().split(" "))
if (a+b<=c):
    print((a+b)*2-1)
elif (b+c<=a):
    print((b+c)*2-1)
elif (c+a<=b):
    print((c+a)*2-1)
else:
    print(a+b+c)