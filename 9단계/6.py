import sys
def is_prime(num, prime): # 소수 인지 아닌지 판별하는 함수 
    if num in prime:
        return True
    else:
        return False
    
def Goldbach_conjecture(n ,prime):
    num_1 = int(n/2)
    num_2 = int(n/2)
    while True:
        if is_prime(num_1,prime) and is_prime(num_2,prime):
            break
        else:
            num_1 -=1
            num_2 +=1
    print(num_1,num_2)
    
def main():
    # is_prime에 아래를 넣으면 매 회마다 에라토스테네스 체를 실행해야해서 비효율적
    # 한꺼번에 검사해놓고 소수를 판별하는 것이 좋다.
    prime = [0] * 10000
    for i in range(2,10000):
        prime[i] = i
    for i in range(2,10000):
        if prime[i] == 0:
            continue
        for j in range( i*2, 10000, i):
            prime[j] = 0
        
    T = int(sys.stdin.readline())
    for i in range(0,T):
        n = int(sys.stdin.readline())
        Goldbach_conjecture(n,prime)
        
main()

# 4  2,2   
# 6  3,3   
# 8  3,5   
# 10 5,5   
# 12 5,7   
# 14 7,7   
# 16 5,11  
# 18 7,11  
# 20 7,13  
# 22 11,11 
# 24 11.13  
# 26 13,13
# 28 11,17
# 30 13,17
