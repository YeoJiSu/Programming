import sys
def main():
    num = int(sys.stdin.readline())
    print(fac(num))

def fac(num):
    if num == 0:
        return 1
    return num*fac(num-1)
    
main()

