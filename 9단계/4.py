import sys
import math

def is_prime(M,N): # 시간 초과 남
    for x in range(M,N+1):
        prime_count = 0
        for i in range(2,x):
            if (x%i == 0):
                prime_count=1
                break
        if (prime_count==0):
            print(x)
            
def is_prime_sqrt(M,N):
    for x in range(M,N+1):
        n = int(math.sqrt(x))
        prime_count = 0
        for i in range(2,n+1):
            if (x%i == 0):
                prime_count=1
                break
        if (prime_count==0):
            print(x)
            
def sieve_of_eratosthenes(M,N):
    prime=[0]*(N+1)
    
    for i in range(2,N+1):
        prime[i]=i

    for i in range(2,N+1):
        if (prime[i] == 0):
            continue;
        for j in range(2*i, N+1, i):
            prime[j] = 0;

    for i in range(M,N+1):
        if prime[i] != 0:
            print(prime[i])
def main():
    M, N = map(int, sys.stdin.readline().split(" "))
    sieve_of_eratosthenes(M,N)
   
main()


