import sys
import math
def main():
    n, k = map(int,sys.stdin.readline().split(" "))
    pascal(n,k) # print(fact(n,k))
    
def fact(n,k): # 팩토리얼로 풀기
    return (math.factorial(n)//(math.factorial(k)*math.factorial(n-k)))%10007

def pascal(n,k): # 파스칼 공식 이용해서 풀기 
    pa = [[0 for _ in range(n+1)] for _ in range(n+1)]
    for i in range(0,n+1):
        for j in range(0,n+1):
            if j == 0 or i == j:
                pa[i][j] =1
            elif j == 1:
                pa[i][j] =i
            elif n>=k:
                pa[i][j] = pa[i-1][j-1] + pa[i-1][j]
            
    print(pa[n][k]%10007)

main()