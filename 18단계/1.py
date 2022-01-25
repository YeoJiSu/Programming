import sys
arr = []
def main():
    num = int(sys.stdin.readline())
    for i in range(0,num):
        order = sys.stdin.readline().split("\n")[0]
        stack(order)
def stack(order):
    if order == "pop":
        if len(arr)==0:
            print(-1)
        else:
            print(arr[-1])
            del arr[-1]
    elif order == "size":
        print(len(arr))
    elif order == "empty":
        if len(arr)==0:
            print(1)
        else:
            print(0)
    elif order == "top":
        if len(arr)==0:
                print(-1)
        else:
            print(arr[-1])
    else: #push 인 경우
        num = int(order.split(" ")[1])
        arr.append(num)
    
main()