import sys


# i_array = [int(x) for x in sys.stdin.readline().split(',')]
# i_array.sort()
# i_max = i_array[-1] 
# cnt = 0

# i_array = []
# i_max = 0
# for a in range(1, 10):
#     i_input = int(sys.stdin.readline())

#     try:
#         if i_input > i_array[-1]:
#             i_array.append(i_input)
#             i_max = a
#     except:
#         i_array.append(i_input)
#         # i_array.insert(i_input)

# print(i_array)
# print(i_max)
# if i_array[a] == i_max:
#     cnt = a  + 1
        
# print(i_max)
# print(cnt)

arr = []
for i in range(9):
    arr.append(int(input()))

print(max(arr))
print(arr.index(max)+1)