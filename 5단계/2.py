import sys
my_list = []
try:
    for i in range(0,9):
        num = int(sys.stdin.readline())
        my_list.append(num)
    sort = sorted(my_list)
    print(sort[-1])
    print(my_list.index(sort[-1])+1)
except:
    print("error")
    exit()