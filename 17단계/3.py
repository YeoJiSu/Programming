import sys
import math

A, B =map(int,sys.stdin.readline().split(" "))

def gcd_lcm(a,b):
    if b == 0: 
        print(a) # gcd 출력하기
        print(math.floor(A*B/a)) # lcm 출력하기 
        return
    gcd_lcm(b,a%b)

gcd_lcm(A,B)      
    