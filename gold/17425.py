import sys

def sum_divisor(n):
    for i in range(n):
        num = int(sys.stdin.readline())
        sum = 0
        for j in range(1,num+1):
            sum+=(num//j)*j
        print(sum)
        
def advanced_sum_divisor(n):
    # 테스트 케이스의 개수가 주어져있으므로  T(1 ≤ T ≤ 100,000) 임의로 합 배열 생성
    my_divisor = [0 for _ in range(1000001)]
    for i in range(1, 1000001):
        for j in range(i, 1000001, i):
            my_divisor[j] += i # 각 숫자에 대한 약수들의 합
        my_divisor[i] += my_divisor[i-1] # 각 숫자까지의 약수들의 합의 합 !
    for k in range(n):
        print(my_divisor[int(sys.stdin.readline())])
    
if __name__=="__main__":
    num = int(sys.stdin.readline())
    # sum_divisor(num) # 시간 초과 에러 발생
    advanced_sum_divisor(num)

