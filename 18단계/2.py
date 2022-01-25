import sys
arr = []
def main():
    num = int(sys.stdin.readline())
    for i in range(0,num):
        a = int(sys.stdin.readline())
        if a==0:
            if len(arr)!=0:
                del arr[-1]
        else:
            arr.append(a)
    print(sum(arr))

main()