# 2501번 - 약수 구하기
import sys
N, K = map(int, sys.stdin.readline().split(' '))
count = 0
for i in range(1,N+1):
    if N%i ==0:
        count+=1
    if count == K:
        print(i)
        exit()
print(0)