import sys
import math
def count():
    num = int(sys.stdin.readline())
    n = int(math.sqrt(num))
    while True:
        if n*(n+1)//2 > num :
            break
        n+=1
    n-=1
    print(n)

if __name__=="__main__":
    count()