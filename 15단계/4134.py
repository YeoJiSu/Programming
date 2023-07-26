# 백준 4134번 - 다음 소수
import sys
import math
n = int(sys.stdin.readline())

def prime_number(n):
    if n<=2 :
        return 2
    k = n
    while True:
        is_prime = True
        for i in range(2,int(math.sqrt(k))+1):
            if k % i == 0:
                is_prime = False
                break
        if is_prime == True:
            return k
        if is_prime == False:
            k+=1
            
for i in range(n):
    print(prime_number(int(sys.stdin.readline())))
