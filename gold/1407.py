
import sys
import math
A, B = map(int, sys.stdin.readline().split(" "))
def count(x):
    result = 0
    index = 1
    while (x != 0):
        if (x%2 != 0) :
            result += (x//2+1)* index
        else :
            result += (x//2)* index
        x //= 2
        index *= 2
    return result
print(count(B)-count(A-1))

#  시간 초과 나는 코드
# count = 0
# for i in range(A,B+1):
#     if i%2!=0: # 홀수라면 +1
#         count+=1
#     else:
#         # 홀수가 아니라면 
#         count_pow = 0
#         while i%2==0:
#             i = i/2
#             count_pow += 1
#         count += 2** count_pow
        
# print(count)
        