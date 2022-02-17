import sys
import math

def SOD(n):
    if n ==1:
        return 0
    my_SOD = []
    for i in range(2,int(math.sqrt(n))+1):
        if n%i == 0:
            my_SOD.append(i)
            my_SOD.append(n//i)
    my_SOD = set(my_SOD) # set을 이용해 중복제거
    return sum(list(my_SOD))

def CSOD(n):
    sum = 0
    for i in range(1,n+1):
        sum+=SOD(i)
    print(sum % 1000000)

def advanced_CSOD(n):
    total = 0
    for i in range(1, n+1):
        total += (n//i)*i
    print((total - (n*(n+1)//2 + n -1))%1000000)

if __name__ == "__main__":
    n = int(sys.stdin.readline())
    # CSOD(n) # -> 시간 초과 에러나는 코드임
    advanced_CSOD(n)


# < 풀이과정 > 
# 1) N의 배수는 N을 항상 약수로 갖는다.
# 2) N이하의 자연수 중에서 i를 약수로 갖는 개수는 N/i개 이다.
#   ex) 12 이하의 자연수 중에서 3을 약수로 갖는 수의 개수는 4개이다 !!
#       그럼 그 4개에 "3"만 곱하면 합이 나오므로 -> " 12/3 * 3 " 이 특정 i(3)일때의 합 경우다.
# 
# 결론 : g(N)=1×N/1+2×N/2+...+N×N/N


