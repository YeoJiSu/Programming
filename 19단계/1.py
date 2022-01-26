import sys
arr = []
count = 0
def main():
    num = int(sys.stdin.readline())
    for i in range(0,num):
        order = sys.stdin.readline().split("\n")[0]
        stack(order)
def stack(order):
    global count
    if order == "pop":
        if len(arr)-count ==0:
            print(-1)
        else:
            print(arr[count]) # 그 다음번엔 count가 1 증가하지
            count+=1 # del arr[0]
            # 여기서 delete/pop을 안해야 시간 초과 에러가 안남 
    elif order == "size":
        print(len(arr)-count)
    elif order == "empty":
        if len(arr)-count==0:
            print(1)
        else:
            print(0)
    elif order == "front":
        if len(arr)-count==0:
                print(-1)
        else:
            print(arr[count])
    elif order == "back":
        if len(arr)-count==0:
                print(-1)
        else:
            print(arr[-1])        
    else: #push 인 경우
        num = int(order.split(" ")[1])
        arr.append(num)
    
main()