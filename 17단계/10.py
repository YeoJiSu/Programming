import sys
    

def main():
    test = int(sys.stdin.readline())
    for i in range(0,test):
        name = []
        cloth = []
        n = int(sys.stdin.readline())
        for i in range(0,n):
            c = sys.stdin.readline().split(" ")[1]
            if c in name:
                cloth[name.index(c)]+=1
            else:
                name.append(c)
                cloth.append(1)
        mul = 1
        for i in cloth:
            mul*=(i+1)
        print(mul-1)
            
main()