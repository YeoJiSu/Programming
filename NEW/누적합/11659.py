import sys
N, M = map(int, sys.stdin.readline().split(" "))
arr = list(map(int, sys.stdin.readline().split(" ")))

value = 0
sum_arr = [0] # 시간초과를 해결하기 위해 1 ~ 현재위치까지의 합을 저장할 배열을 초기화한다. 
for i in arr:
    value+=i
    sum_arr.append(value)
for i in range(M):
    i, j = map(int, sys.stdin.readline().split(" "))
    print(sum_arr[j]-sum_arr[i-1])