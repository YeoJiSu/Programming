# 백준 17103번 - 골드바흐 파티션
import sys

# 에라토스테네서의 체 
N = 1000001
_list = [1 for i in range(N)]
_list[0] = 0
_list[1] = 0
for num in range(2,N//2):
    if _list[num] ==0: # 해당 if문을 아래의 for문에 넣어서 계속 시간초과났음. 
        continue
    for j in range(num*2,N,num):
        _list[j] = 0


n = int(sys.stdin.readline())

for i in range(n):
    T =  int(sys.stdin.readline())
    count = 0
    for j in range(2,int(T//2)+1):
        if _list[j] == 1 and _list[T-j] == 1:
            count+=1
    print(count)
    
"""
# 아래는 시간 초과 발생하는 코드
import math

def is_prime(n):
    for i in range(2, int(math.sqrt(n))+1):
        if n%i == 0:
            return False
    return True

n = int(sys.stdin.readline())

for i in range(n):
    T =  int(sys.stdin.readline())
    count = 0
    for j in range(2,int(T//2)+1):
        if is_prime(j)==True and is_prime(T-j)==True:
            count+=1
    print(count)
"""

