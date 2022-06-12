import sys

def four_squares(num):
    if (num**0.5 == int(num**0.5)):
        return 1
    for i in range(1, int(num**0.5)+1):
        if ((num-i**2)**0.5 == int((num-i**2)**0.5)):
            return 2
    for i in range(1, int(num**0.5)+1):
        for j in range(1, int((num-i**2)**0.5)+1):
            if ((num-i**2-j**2)**0.5 == int((num-i**2-j**2)**0.5)):
                return 3
    return 4
    
num = int(sys.stdin.readline())
print(four_squares(num))

# 오류 있는 코드 
# count=[]
# while num>0:
#     sqrt= int(math.sqrt(num))
#     num-=sqrt**2
#     if sqrt not in count:
#         count.append(sqrt)
# print(len(count))