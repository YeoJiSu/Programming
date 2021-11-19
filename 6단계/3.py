import sys
import math
def main():
    try:
        num=int(sys.stdin.readline())
        print(find(num))
    except:
        exit()
        
def find(x):
    # 일의자리 십의 자리 수는 한수임 
    if (x/10<10):
        return(x)
    
    # 100의 자리 숫자는 이렇게 계산함 
    count=99
    for i in range(100,x+1):
        
        a=math.floor(i/10/10)%10
        b=math.floor(i/10)%10
        c=i%10
        if (a-b)==(b-c):
            count+=1 
    # 1~1000까지 수를 받는데 1000은 한수 아니므로 1빼기 
    if (x==1000):
        count-=1
    return count

main()