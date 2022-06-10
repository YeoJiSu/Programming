# 동적 계획법으로 푼 문제
import sys
N,M = map(int,sys.stdin.readline().split(' '))
arr = []
for i in range(N):
    line = list(map(int, sys.stdin.readline().split(' ')))
    for i in range(len(line)-1):
        line[i+1] += line[i]
    arr.append(line)

# 각 index까지의 합을 담을 배열
sum_arr = arr
for i in range(N-1):
    for k in range(N):
        sum_arr[i+1][k] += arr[i][k]

for i in range(M):
    x1,y1,x2,y2 = map(int, sys.stdin.readline().split(' '))
    x1-=1
    y1-=1
    x2-=1
    y2-=1
    if (x1==0 and y1 ==0):
        print(sum_arr[x2][y2])
    elif (x1 == 0):
        print(sum_arr[x2][y2]-sum_arr[x2][y1-1])
    elif (y1 ==0):
        print(sum_arr[x2][y2] - sum_arr[x1-1][y2])
    else:
        print(sum_arr[x2][y2]+sum_arr[x1-1][y1-1] - sum_arr[x1-1][y2]-sum_arr[x2][y1-1])

