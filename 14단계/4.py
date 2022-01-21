import sys
N,M = map(int, sys.stdin.readline().split(" "))

visit = [0]*(N+1)
arr = [0]*(M+1)

def count(num,index):
    if index == M+1:
        for i in range(1,M+1):
            print( arr[i], end=" ")
        print()
    else:
        for i in range(num,N+1):
            arr[index]=i
            count(i,index+1)
                
count(1,1)