import sys
def main():
    n, k = map(int,sys.stdin.readline().split(" "))
    comb(n,k)
    
def comb(n,k):
    mul = 1
    for i in range(0,k):
        mul*=n
        mul/=(i+1)
        n-=1
    print(int(mul))

main()