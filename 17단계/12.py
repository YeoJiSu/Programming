import sys
import math
def main():
    n,m =map(int, sys.stdin.readline().split())
    print(comb(n,m))

def comb(n,m):
    two = fac_num(n,2)-fac_num(m,2)-fac_num(n-m,2)
    five = fac_num(n,5)-fac_num(m,5)-fac_num(n-m,5)  
    return min(two,five)

# 1부터 num 까지 들어있는 i개수
def fac_num(num, i): # i는 2, 5 
    count = 0
    while num>0:
        num = num//i
        count += num
    return count
main()