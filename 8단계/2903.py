# 2903번 - 중앙 이동 알고리즘
import sys
N = int(sys.stdin.readline())
answer = 4

start = 1
count = 2
for i in range(N):
    answer += start*count + (start*2+1)*(count-1)
    start*=2
    count=count*2-1
print(answer)