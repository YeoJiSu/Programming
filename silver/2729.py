import sys
def binary(a,b):
    total = a+b
    total_list = list(str(total))
    
    for i in range(len(total_list)-1,0,-1):
        if int(total_list[i])==2:
            total_list[i] = str(0)
            total_list[i-1] = str(int(total_list[i-1])+1)
        elif int(total_list[i])==3:
            total_list[i] = str(1)
            total_list[i-1] = str(int(total_list[i-1])+1)
    
    if int(total_list[0])==0:
        print("0",end="")
    elif int(total_list[0])==1:
        print("1",end="")
    elif int(total_list[0])==2:
        print("10",end="")
    elif int(total_list[0])==3:
        print("11",end="")
    for i in range(1,len(total_list)):
        print(total_list[i],end="")
    print()
   
def input_num():
    num = int(sys.stdin.readline())
    for i in range(num):
        a, b = map(int,sys.stdin.readline().split())
        binary(a,b)
if __name__ == "__main__":
    input_num()