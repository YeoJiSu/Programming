# 좌표 압축
import sys
N  = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
arr_indexing = [[arr[i],i,0] for i in range(N)]

arr_indexing.sort(key=lambda x:x[0])

count = 0
for k in range(0,N-1):
    if (arr_indexing[k][0]<arr_indexing[k+1][0]):
        count+=1
        arr_indexing[k+1][2] = count
    elif (arr_indexing[k][0] == arr_indexing[k+1][0]):
        arr_indexing[k+1][2] = count

arr_indexing.sort(key=lambda x:x[1])

for i in arr_indexing:
    print(i[2], end=" ")