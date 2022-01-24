import sys
import math

def mod(arr):
    interval = []
    for i in range(1,len(arr)):
        interval.append(arr[i]-arr[i-1])
    
    my_gcd = interval[0]
    for i in range(1, len(interval)):
        my_gcd = math.gcd(my_gcd, interval[i])

    answer = []
    for i in range(2, int(math.sqrt(my_gcd))+1):
        if my_gcd%i==0:
            answer.append(i)
            answer.append(int(my_gcd/i))
    answer.append(my_gcd)
    answer = sorted(list(set(answer)))
    print(*answer)
    
    
def main():
    num = int(sys.stdin.readline())
    arr = []
    for i in range(0,num):
        a = int(sys.stdin.readline())
        arr.append(a)
    mod(sorted(arr))
main()