# 백준 19532번: 수학은 비대면강의입니다.
import sys
a,b,c,d,e,f = map(int, sys.stdin.readline().split(' '))
"""
x = (c*e - b*f) / (a*e - b*d)
y = (c-a*x)/b 또는 y = (f-d*x)/e 
"""
x = (c*e - b*f) / (a*e - b*d)
x = int(x)

if b != 0:
     y = (c-a*x)/b
elif e !=0:
     y = (f-d*x)/e
y = int(y)

print(x, y)