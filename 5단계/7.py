import sys

def main():
    try:
        classes = int(sys.stdin.readline())       
        problem(classes)
    except:
        exit()
        
def problem(x):
    for i in range(0,x):
        each = list(map(int, sys.stdin.readline().split()))
        print("{:.3f}%".format(round(rate(each),3)))

def rate(x):
    count = 0
    ave = (sum(x)-x[0])/x[0]
    for i in range(1, len(x)):
        if x[i]>ave:
            count+=1
    return count/int(x[0])*100
    
        
main()