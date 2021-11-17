import sys
import math
mul =1
my_list = [0]*10

def main():
    global mul
    try:
        for i in range(0,3):
            num = int(sys.stdin.readline())
            mul*=num
        count(mul)
        list_print(my_list)
        
    except:
        print("error")
        exit()

def count(x):
    my_list[x%10]+=1
    x = math.floor(x/10)
    if (x == 0):
        return 0
    count(x)
    
def list_print(x):
    for i in range(0,len(x)):
        print(x[i])

main()