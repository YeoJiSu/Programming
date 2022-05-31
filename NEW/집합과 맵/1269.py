import sys
A, B = map(int, sys.stdin.readline().split(" "))
A_set = set(map(int,sys.stdin.readline().split(" ")))
B_set = set(map(int,sys.stdin.readline().split(" ")))
print(len(A_set-B_set)+len(B_set-A_set))