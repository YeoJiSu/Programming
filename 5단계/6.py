import sys

# 연속되는 값들의 합을 return 
def my_sum(x):
    sum=0
    for i in range(1,x+1):
        sum+=i
    return sum


def problem(x):
    for i in range(0,x):
        # OX 들 입력하기 
        my_list = sys.stdin.readline()
        # X를 기준으로 자르고 
        new = my_list.split("X")
        result = 0
        for j in range(0, len(new)):
            O_count = len(new[j])
            if j==len(new)-1:
                O_count-=1
            result += my_sum(O_count)
        print(result)
        
# main 함수 
def main():
    try:
        num = int(sys.stdin.readline())
        problem(num)
        
    except:
        exit()    
            
main()