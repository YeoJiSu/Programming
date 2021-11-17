import sys
try:
    count = int(sys.stdin.readline())
    my_list = list(map(int, sys.stdin.readline().split()))
    print(sorted(my_list)[0],sorted(my_list)[-1])
except:
    print("error")
    exit()