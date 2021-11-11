import sys


cnt = int(sys.stdin.readline())

i_array = [int(x) for x in sys.stdin.readline().split()]
new_array = []
for a in range(0, cnt):
    if len(i_array) < a:
        break;
    
    new_array.append(i_array[a])


new_array.sort()

print("{} {}".format(new_array[0], new_array[-1]))
