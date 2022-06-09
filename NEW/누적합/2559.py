import sys
N, K = map(int, sys.stdin.readline().split(" "))
arr = list(map(int, sys.stdin.readline().split(" ")))

initial = sum(arr[:K])
result = initial
for k in range(1,N-K+1):
    total = initial - arr[k-1] + arr[k+K-1]
    if total > result:
        result = total
    initial = total
print(result)