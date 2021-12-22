import sys
def main():
    num = int(sys.stdin.readline())
    if num>20 or num<0:
        exit()
    print(fibo(num))

def fibo(num):
    if num == 0:
        return 0
    if num == 1:
        return 1
    return fibo(num-2)+fibo(num-1)
    
main()

