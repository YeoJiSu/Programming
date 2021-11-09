import sys


def getCount():
    i_count = int(sys.stdin.readline())

    if i_count > 100000:
        getCount()
    
    return i_count

if __name__ =='__main__':
    n = getCount()
    
    for i in range(n, 0, -1):
        print(i)