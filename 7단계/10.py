import sys
def main():
    try:
        sum=0
        num=int(sys.stdin.readline())
        for i in range(0,num):
            str =sys.stdin.readline().split("\n")[0]
            if (count(str)==True):
                sum+=1
        print(sum)
    except:
        exit()
    
def count(str1):
    alpha=[]
    for j in str1:
        if j not in alpha:
            alpha.append(j) 
        else:
            if (j!=alpha[-1]):
                return False
    return True

main()

