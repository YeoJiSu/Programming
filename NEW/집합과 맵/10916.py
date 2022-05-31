import sys
N = int(sys.stdin.readline())
N_arr = list(map(int, sys.stdin.readline().split(" ")))
M = int(sys.stdin.readline())
M_arr = list(map(int, sys.stdin.readline().split(" ")))
counter = {}
for i in N_arr:
    if i not in counter:
        counter[i]=1
    else: 
        counter[i]+=1
for k in M_arr:
    if k not in counter:
        print(0, end=" ")
    else:
        print(counter[k], end=" ")
