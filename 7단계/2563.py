# 백준 2563번 - 색종이
import sys
paper = [[0 for i in range(100)]for j in range(100)]
N = int(sys.stdin.readline())

_sum = 0
for i in range(N):
    a,b = map(int, sys.stdin.readline().split(" "))
    for j in range(a,a+10):
        for k in range(b,b+10):
            if paper[j][k] == 0:
                paper[j][k]=1
                _sum+=1
print(_sum)

    
    