import math
a = int(input())
cycle = 0
def my_cycle(x):
    sum = math.floor(x/10)+x%10
    new = x%10*10 + sum%10
    global cycle 
    cycle+=1
    if (new == a):
        print(cycle)
        exit()
    my_cycle(new)

def main():
    my_cycle(a)

main()
    

