import sys


# i_array = [int(x) for x in sys.stdin.readline().split()]

a = int(sys.stdin.readline())
b = int(sys.stdin.readline())
c = int(sys.stdin.readline())
result = a * b * c
# for i in range(0, len(i_array)):
#     result = result * i_array[i]

# result = 17037300
result = list(str(result))

for i in range(0, 10):
    print(result.count(str(i)))