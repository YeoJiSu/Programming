import sys
num = int(sys.stdin.readline())
my_list = []
for j in range(num):
    my_str = sys.stdin.readline().split("\n")[0]
    is_str = False
    for i in range(0,len(my_list)):
        if my_list[i][1] == my_str:
            my_list[i][0]+=1
            is_str = True
            break
    
    if is_str == False:
        my_list.append([1,my_str])
my_list.sort(reverse=True)
my_list = sorted(my_list, key=lambda x: x[0])
print(my_list[-1][1])