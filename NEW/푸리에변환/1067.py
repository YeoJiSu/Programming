import sys
N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split(' ')))
B = list(map(int, sys.stdin.readline().split(' ')))
max_value = 0
for i in range(N):
    value = 0
    for j in range(N):
        k=j-i
        value+=A[j]*B[k]
    max_value = max(value, max_value)
print(max_value)