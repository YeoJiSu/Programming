import sys
my_list = []

def main():
    try:
        for i in range(0,10):
            num = int(sys.stdin.readline())
            count(num)
        print(len(my_list))
    except:
        exit()
    
def count(x):
    x=x%42
    if x not in my_list:
        my_list.append(x)
main()