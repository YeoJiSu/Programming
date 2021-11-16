import sys
N, X = map(int, sys.stdin.readline().split())
m = list(map(int, sys.stdin.readline().split()))
for i in range(0,N):
    if m[i] < X:
        print(m[i])