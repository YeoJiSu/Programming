import sys
def main():
    num = int(sys.stdin.readline())
    count(fac(num))
def fac(num):
    if num>1:
        return num*fac(num-1)
    else:
        return 1
def count(num):
    
    stn = str(num)
    l = len(stn)
    count = 0
    for i in range(0,l-1):
        if (stn[l-i-1])== "0":
            count+=1 
            if (stn[l-i-2])!="0":
                break
        
    print(count)
    
main()