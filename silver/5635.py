import sys
num = int(sys.stdin.readline())
name_arr = []
birth_arr = []
for i in range(num):
    name, dd, mm, yyyy = map(str, sys.stdin.readline().split(' '))
    name_arr.append(name)
    birth_arr.append(int(yyyy)*10000 + int(mm)*100+int(dd))
print(name_arr[birth_arr.index(max(birth_arr))])
print(name_arr[birth_arr.index(min(birth_arr))])