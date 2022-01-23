import sys

def relation(a,b):
    if a%b == 0:
        print("multiple")
    elif b%a == 0:
        print("factor")
    else:
        print("neither")

def main():
    while True:
        a, b = map(int,sys.stdin.readline().split(" "))
        if (a,b) == (0,0):
            exit()
        relation(a,b)
        

main()        