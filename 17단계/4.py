import sys
import math
def gcd(a,b):
    if b==0:
        return a
    return gcd(b,a%b)
    
def main():
    num = int(sys.stdin.readline())
    for i in range(0,num):
        a, b = map(int, sys.stdin.readline().split(" "))
        print(math.floor(a*b/gcd(a,b)))
main()