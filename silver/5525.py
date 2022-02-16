import sys
def IOI_number(num):
    return("I"+"OI"*num)

# 시간 복잡도 O(num * str_len)
def count_IOI(): # 시간 초과 문제
    num = int(sys.stdin.readline())
    IOI_num = IOI_number(num)
    str_len = int(sys.stdin.readline())
    my_str = sys.stdin.readline().split("\n")[0]
    IOI_len = len(IOI_num)
    count = 0
    for i in range(0,str_len-IOI_len+1):
        if(my_str[i:IOI_len+i] == IOI_num):
            count+=1
    print(count)

# 시간 복잡도 O(str_len)
def advance_count_IOI():
    num = int(sys.stdin.readline()) 
    str_len = int(sys.stdin.readline())
    my_str = sys.stdin.readline().split("\n")[0]
    
    pattern = 0
    count=0
    i=1
    while i <str_len-1 :
        if my_str[i-1] == "I" and my_str[i] == "O" and my_str[i+1] == "I":
            pattern+=1
            i+=1
            if pattern == num:
                count+=1
                pattern -= 1
        else:
            pattern = 0
        i+=1
    print(count)
if __name__ == "__main__":
    advance_count_IOI()