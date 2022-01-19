import sys

def count_prime(n):
    # n 보다 크고 2*n 보다 작거나 같은 소수 개수 출력하기
    m = 2*n
    prime = [0]* (m+1)
    for i in range(2,m+1):
        prime[i] = i
    
    for i in range(2,m+1):
        if (prime[i]==0):
            continue
        for j in range(2*i,m+1,i):
            prime[j] = 0
    
    count= 0
    for i in range(n+1, m+1):
        if prime[i] != 0:
            count+=1
    print(count)
    
def main():
    while True:
        n = int(sys.stdin.readline())
        if n==0:
            break
        count_prime(n)
main()