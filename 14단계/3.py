import sys
N, M  = map(int, sys.stdin.readline().split(" "))
seq = [0]*(M+1) # 예를 들어 3

def sequence(x):
    if x == M+1:
        for i in range(1,M+1):
            print(seq[i], end=" ")
        print()
    else:
        for i in range(1, N+1):
            seq[x]=i
            sequence(x+1)
            seq[x]=0
sequence(1)