import sys
def gcd(a,b):
    if b==0:
        return a
    return gcd(b, a%b)

def gcd_sum():
    num = int(sys.stdin.readline())
    for i in range(num):
        array = list(map(int,sys.stdin.readline().split()))
        sum = 0
        for i in range(1,len(array)-1):
            for j in range(i+1, len(array)):
                sum+=gcd(array[i], array[j])
        print(sum)
        
if __name__ == "__main__":
    gcd_sum()