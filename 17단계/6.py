import sys

def gcd(a,b):
    if b==0:
        return a
    return gcd(b,a%b)

def mod(arr):
    for i in range(1, len(arr)):
        g = gcd(arr[0],arr[i])
        print("%d/%d"%(int(arr[0]/g),int(arr[i]/g)))

def main():
    num = int(sys.stdin.readline())
    my = list(map(int,sys.stdin.readline().split(" ")))
    mod(my)

main()
