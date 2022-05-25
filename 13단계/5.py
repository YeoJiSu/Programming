#2477번 - 참외밭
import sys
N = int(sys.stdin.readline())
where_array = []
length_array = []
index = []

for i in range(0,6):
    where, length = map(int,sys.stdin.readline().split(" "))
    where_array.append(where)
    length_array.append(length)

for k in where_array:
    if (where_array.count(k)==1):
        index.append(where_array.index(k))
if (index[0]+1==index[1]):
    small = length_array[index[0]-2] * length_array[index[0]-3]
else:
    small = length_array[index[1]-2] * length_array[index[1]-3]
big = length_array[index[0]] * length_array[index[1]]

print((big-small)*N)
