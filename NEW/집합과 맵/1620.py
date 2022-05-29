import sys
N, M = map(int, sys.stdin.readline().split(" "))
arr = {}
arr_reversed = {} # arr에서 key - value를 뒤집은 배열 -> 그래야 시간초과 발생하지 않음
for i in range(N):
    value = sys.stdin.readline().split("\n")[0]
    arr[i]=value
    arr_reversed[value] = i
for k in range(M):
    value = sys.stdin.readline().split("\n")[0]
    if (value.isdigit()):
        print(arr[int(value)-1])
    else:
        print(arr_reversed[value]+1) 