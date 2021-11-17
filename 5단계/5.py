import sys

def main():
    try:
        subject = int(sys.stdin.readline())
        my_list = list(map(int, sys.stdin.readline().split()))
        print(ave(my_list))
    except:
        exit()
        
def ave(x):
    max1 = sorted(x)[-1]
    new = sum(x)/len(x)/max1*100
    return new
main()
