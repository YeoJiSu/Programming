#재귀 2447번: 별 찍기 - 고민 많이 했던 문제
import math
N = int(input())

# # 시간 초과 나는 코드
# def star(i,j,x):
#     if ((i//x)%3==1 and (j//x)%3==1):
#         print(" ",end="")
#     else:
#         if (x//3==0):
#             print("*",end="")
#         else:
#             star(i,j,x//3)
    

# for i in range(N):
#     for j in range(N):
#         star(i,j,N)
#     print()

# # 해결한 코드 - 배열에 담아서 
def star(x,arr):
    if (x==3):
        return arr
    new_arr = []
    for i in arr:
        new_arr.append(i*3)
    for i in arr:
        new_arr.append(i+" "*len(arr)+i)
    for i in arr:
        new_arr.append(i*3)
    return star(x//3,new_arr)
first = ["***","* *","***"]
final = star(N,first)
for i in final:
    print(i)
